import csv
import ujson
from copy import copy

from io import StringIO
from defusedxml.ElementTree import parse
from abc import ABCMeta, abstractmethod
from typing import AnyStr, Any, Dict, Union, Type, List

from marinetrafficapi.constants import (MiscConst, ResponseConst,
                                        FormatterConst, ResponseDataConst)


class Formatter(metaclass=ABCMeta):
    """Abstract formatter class."""

    def __init__(self, response):
        self._response = response

    @abstractmethod
    def _format(self, data: AnyStr) -> Any:
        """Format method in formatter classes."""

        return data

    def format(self, data: AnyStr) -> Any:
        """Main format method."""

        return self._format(data)

    @abstractmethod
    def _format_meta(self, data: AnyStr) -> Any:
        """Format method in formatter classes."""

        return data

    def format_meta(self, data: AnyStr) -> Any:
        """Main format method."""

        return self._format_meta(data)

    @staticmethod
    def _to_list(data: AnyStr) -> List:
        """To list method in formatter classes."""

        return data

    def to_list(self, data: AnyStr) -> List:
        """Main to list method."""

        return self.__class__._to_list(data)

    @staticmethod
    def _default_meta_data(total_results: int) -> Dict:
        """Create default data set if there aren't one from the response."""

        return {
            ResponseDataConst.TOTAL_RESULTS: total_results,
            ResponseDataConst.TOTAL_PAGES: 1,
            ResponseDataConst.CURRENT_PAGE: 1
        }

    @staticmethod
    def _meta_data_to_int(meta_data: Dict) -> Dict:
        """Cast all data to int."""

        return {
            ResponseDataConst.TOTAL_RESULTS:
                int(meta_data.get(ResponseDataConst.TOTAL_RESULTS, 1)),
            ResponseDataConst.TOTAL_PAGES:
                int(meta_data.get(ResponseDataConst.TOTAL_PAGES, 1)),
            ResponseDataConst.CURRENT_PAGE:
                int(meta_data.get(ResponseDataConst.CURRENT_PAGE, 1)),
        }


class Json(Formatter):
    """JSON data formatter class."""

    def _format(self, data: AnyStr) -> Dict:
        """Transform raw data from server into python native type."""

        formatted_data = ujson.loads(data)
        if isinstance(formatted_data, dict):
            return formatted_data.get(ResponseDataConst.DATA, formatted_data)
        else:
            return formatted_data

    def _format_meta(self, data: AnyStr) -> Dict:
        """Transform raw data from server into python native type."""

        formatted_data = ujson.loads(data)
        if isinstance(formatted_data, dict):
            return formatted_data.get(ResponseDataConst.META, {})
        else:
            return self.__class__._default_meta_data(len(formatted_data))


class Csv(Formatter):
    """CSV data formatter class."""

    def _format(self, data: AnyStr) -> Union[List, Dict]:
        """Transform raw data from server into python native type."""

        io_data = StringIO(data)
        data = list(csv.reader(io_data))

        # Check for error response
        error_response = self.__class__.__get_error_response(data)
        if error_response:
            return error_response

        # Check if the response came with meta data
        csv_data = self.__get_data_or_meta(data)

        return self.__class__.__format(csv_data)

    def _format_meta(self, data: AnyStr) -> Any:
        """Format method in formatter classes."""

        io_data = StringIO(data)
        data = list(csv.reader(io_data))

        # Check if the response came with meta data
        csv_data = self.__get_data_or_meta(data, meta=True)

        meta_data = self.__class__.__format(csv_data)[0]
        return self.__class__._meta_data_to_int(meta_data)

    @staticmethod
    def _default_meta_data(total_results: int) -> List:
        """Create default data set if there aren't one from the response."""

        return [
            [
                ResponseDataConst.TOTAL_RESULTS,
                ResponseDataConst.TOTAL_PAGES,
                ResponseDataConst.CURRENT_PAGE
            ],
            [str(total_results), 1, 1]
        ]

    @staticmethod
    def __get_error_response(data: List) -> Dict:
        """Extracts error part from response."""

        if data[0][0].startswith(ResponseDataConst.ERROR):
            # errors are pure txt message,
            # nothing like csv.
            # trying to follow the same error message
            # structure from json error response.

            return {
                MiscConst.ERRORS: [
                    {
                        ResponseConst.CODE:
                            data[0][0].split('_')[1].split('-')[0],
                        ResponseConst.DETAIL: data[0][0].split('-')[1]
                    }
                ]
            }
        else:
            return {}

    def __get_data_or_meta(self, data: List, meta: bool = False) -> List:
        """Extract data or meta data from response data."""

        csv_keys = data[0]
        if ResponseDataConst.CURRENT_PAGE in csv_keys or \
           ResponseDataConst.TOTAL_PAGES in csv_keys or \
           ResponseDataConst.TOTAL_RESULTS in csv_keys:
            # This means that response data has come with meta data.

            if meta:
                # Take only first two lines from the
                # response to get the meta data part
                return copy(data[:2])
            else:
                # Exclude first two lines from the
                # response to get the data part
                return copy(data[2:])
        else:
            # Response came only with data part
            if meta:
                # Return default meta data
                return self.__class__._default_meta_data(len(data[1:]))
            else:
                # Return data
                return data

    @staticmethod
    def __format(data: List) -> List:
        """Transform list of lists into a list of dicts."""

        csv_data = []
        csv_keys = []

        for i, line in enumerate(data):
            line_data = {}
            if i == 0:
                csv_keys = [k.strip() for k in line]
            else:
                for j, key in enumerate(csv_keys):
                    line_data[key] = line[j]

                # sometimes number of delimiters in data part of
                # csv is bigger then in keys part, so we need
                # to concatenate the rest of the delimited parts
                # of data line.
                if len(csv_keys) < len(line):
                    line_data[csv_keys[-1]] = ','.join(line[len(csv_keys) - 1:])

                csv_data.append(line_data)

        return csv_data


class Xml(Formatter):
    """XML data formatter class."""

    def _format(self, data: AnyStr) -> Union[List, Dict]:
        """Transform raw data from server into python native type."""

        data = parse(StringIO(data))

        xml_data = []
        child_tag = list(data.getroot().iter())[1]

        if child_tag.tag == ResponseDataConst.STATUS:

            child_tag_element = list(child_tag.iter())[1]
            if child_tag_element.tag == ResponseDataConst.ERROR:
                # error message does not follow
                # same structure as data message.
                # trying to follow the same error message
                # structure from json error response.

                attribs = child_tag_element.attrib
                xml_data = {
                    MiscConst.ERRORS: [
                        {
                            ResponseConst.CODE: attribs[ResponseDataConst.CODE],
                            ResponseConst.DETAIL:
                                attribs[ResponseDataConst.DESCRIPTION]
                        }
                    ]
                }
        else:
            xml_data = [child.attrib for child in list(data.iter())[1:]]

        return xml_data

    def _format_meta(self, data: AnyStr) -> Any:
        """Format method in formatter classes."""

        data = parse(StringIO(data))
        meta_data = data.getroot().attrib

        if not meta_data:
            # Taking formatted data from Response object because
            # it keeps the data cached in memory, rather then
            # directly from this class and format it all over again
            total_results = len(
                [child.attrib for child in list(data.iter())[1:]]
            )
            meta_data = self.__class__._default_meta_data(total_results)

        return self.__class__._meta_data_to_int(meta_data)


class FormatterFactory:
    """Formatter factory class."""

    formatters = {
        FormatterConst.JSON: Json,
        FormatterConst.JSONO: Json,
        FormatterConst.XML: Xml,
        FormatterConst.CSV: Csv
    }

    def __init__(self, name: str):
        self._name = name

    def get_formatter(self) -> Union[Type[Json], Type[Xml], Type[Csv], None]:
        """Get the formatter class using string key."""

        return FormatterFactory.formatters.get(self._name)
