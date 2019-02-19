from typing import Any, Type, List, Union

from marinetrafficapi.formatter import Formatter, Json, Xml, Csv


class Response:
    """Response object returned from API call."""

    def __init__(self, data: Any, status_code: int,
                 formatter: Type[Formatter], api_reguest):
        self._data = data
        self._model = api_reguest.model

        self.api_reguest = api_reguest
        self.formatter = formatter()
        self.status_code = status_code

        self._response_data = {
            'to_list': None,
            'formatted': None,
            'models': []
        }

    @property
    def raw_data(self) -> Any:
        """Return data as is from the server."""

        return self._data

    @property
    def formatted_data(self) -> Union[Type[Json], Type[Xml],
                                      Type[Csv], None]:
        """Format data using secected formatter."""

        if self._response_data['formatted'] is None:
            self._response_data['formatted'] = \
                self.formatter.format(self._data)

        return self._response_data['formatted']

    @property
    def models(self) -> Union[List[object], None]:
        """Transform raw data into models."""

        if not self._response_data['models']:
            formatted_data = self.formatter.format(self._data)
            self._response_data['models'] = \
                self._model.process(
                    self.formatter.to_list(formatted_data))
            
        return self._response_data['models']

    @property
    def to_list(self) -> Union[List[object], None]:
        """Transform data into list."""

        if not self._response_data['to_list']:
            formatted_data = self.formatter.format(self._data)
            self._response_data['to_list'] = \
                self.formatter.to_list(formatted_data)

        return self._response_data['to_list']
