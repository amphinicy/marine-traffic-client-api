import csv
import ujson
from lxml import etree
from io import StringIO
from typing import AnyStr, Any, Dict, Union, Type, List


class Formatter:
    """"""

    def __init__(self):
        pass

    def _format(self, data: AnyStr) -> Any:
        """"""

        return data

    def format(self, data: AnyStr) -> Any:
        """"""

        return self._format(data)

    def _to_list(self, data: AnyStr) -> List:
        """"""

        return data

    def to_list(self, data: AnyStr) -> List:
        """"""

        return self._to_list(data)


class Json(Formatter):
    """"""

    def _format(self, data: AnyStr) -> Dict:
        """"""

        return ujson.loads(data)


class Csv(Formatter):
    """"""

    def _format(self, data: AnyStr) -> Union[List, Dict]:
        """"""

        data = list(csv.reader(StringIO(data)))

        csv_data = []

        if data[0][0].startswith('ERROR_'):
            # errors are pure txt message,
            # nothing like csv.
            # trying to follow the error message
            # structure from json error response.

            csv_data = {
                'errors': [
                    {
                        "code": data[0][0].split('_')[1].split('-')[0],
                        "detail": data[0][0].split('-')[1]
                    }
                ]
            }

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
                    line_data[csv_keys[-1]] = ','.join(line[len(csv_keys)-1:])

                csv_data.append(line_data)

        return csv_data


class Xml(Formatter):
    """"""

    def _format(self, data: AnyStr) -> Union[List, Dict]:
        """"""

        data = etree.fromstring(data.encode('utf-8'))

        xml_data = []

        if list(data)[0].tag == 'STATUS':
            if list(list(data)[0])[0].tag == 'ERROR':
                # error message does not follow
                # same structure as data message.
                # trying to follow the error message
                # structure from json error response.

                attribs = list(list(data)[0])[0].attrib
                xml_data = {
                    'errors': [
                        {
                            "code": attribs['CODE'],
                            "detail": attribs['DESCRIPTION']
                        }
                    ]
                }
        else:
            xml_data = [child.attrib for child in data]

        return xml_data


class FormatterFactory:

    formatters = {
        'json': Json,
        'jsono': Json,
        'xml': Xml,
        'csv': Csv
    }

    def __init__(self, name: str):
        self._name = name

    def get_formatter(self) -> Union[Type[Json], Type[Xml], Type[Csv], None]:
        """"""

        return FormatterFactory.formatters.get(self._name)
