from typing import Any, Type, List, Union, TYPE_CHECKING

from marinetrafficapi.formatter import Formatter, Json, Xml, Csv
from marinetrafficapi.constants import (ClientConst, FormatterConst,
                                        ResponseConst)


if TYPE_CHECKING:
    from marinetrafficapi.bind import Api


class Response:
    """Response object returned from API call."""

    def __init__(self, data: Any, status_code: int,
                 formatter: Type[Formatter],
                 api_request: Type['Api']):
        self._data = data
        self._model = api_request.model

        self.api_reguest = api_request
        self.formatter = formatter(self)
        self.status_code = status_code

        self._response_data = {
            ResponseConst.TO_LIST: None,
            FormatterConst.FORMATTED: None,
            ClientConst.MODELS: [],
            ClientConst.META: None
        }

    @property
    def raw_data(self) -> Any:
        """Return data as is from the server."""

        return self._data

    @property
    def formatted_data(self) -> Union[Type[Json], Type[Xml],
                                      Type[Csv], None]:
        """Format data using selected formatter."""

        if self._response_data[FormatterConst.FORMATTED] is None:
            self._response_data[FormatterConst.FORMATTED] = \
                self.formatter.format(self._data)

        return self._response_data[FormatterConst.FORMATTED]

    @property
    def models(self) -> Union[List[object], None]:
        """Transform raw data into models."""

        if not self._response_data[ClientConst.MODELS]:
            formatted_data = self.formatter.format(self._data)
            self._response_data[ClientConst.MODELS] = \
                self._model.process(
                    self.formatter.to_list(formatted_data))
            
        return self._response_data[ClientConst.MODELS]

    @property
    def meta(self) -> Union[List[object], None]:
        """Transform raw data into models."""

        if not self._response_data[ClientConst.META]:
            self._response_data[ClientConst.META] = \
                self.formatter.format_meta(self._data)

        return self._response_data[ClientConst.META]

    @property
    def to_list(self) -> Union[List[object], None]:
        """Transform data into list."""

        if not self._response_data[ResponseConst.TO_LIST]:
            formatted_data = self.formatter.format(self._data)
            self._response_data[ResponseConst.TO_LIST] = \
                self.formatter.to_list(formatted_data)

        return self._response_data[ResponseConst.TO_LIST]
