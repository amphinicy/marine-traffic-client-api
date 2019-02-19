from datetime import datetime
from typing import Any, Union, List, TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from marinetrafficapi.models import Model


class Field:
    """Abstract field class."""

    def __init__(self, index: Union[int, str],
                 desc: str = None, **kwargs):
        self._index = index
        self._desc = desc
        self._kwargs = kwargs

        self.data = None

    def convert_item(self, model: 'Model') -> None:
        """Convert item to desired item type"""

        try:
            self.data = model.item[self._index]
        except IndexError:
            self.data = None
        except KeyError:
            self.data = None

        try:
            self.data = self._convert_field_item(self.data,
                                                 **self._kwargs)
        except TypeError:
            self.data = None

    def _convert_field_item(self, data: Any, **kwargs) -> Any:
        """Actual converting."""


class NumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data: str, **kwargs) -> int:
        """Actual converting."""

        try:
            return int(data)
        except ValueError:
            return 0


class RealNumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data: str, **kwargs) -> float:
        """Actual converting."""

        return float(data)


class TextField(Field):
    """Converting item to string."""

    def _convert_field_item(self, data: str, **kwargs) -> str:
        """Actual converting."""

        return str(data)


class BooleanField(Field):
    """Converting item to boolean."""

    def _convert_field_item(self, data: str, **kwargs) -> \
            Union[bool, None]:
        """Actual converting."""

        if data == '1':
            return True
        elif data == '0':
            return False
        else:
            return None


class DatetimeField(Field):
    """Converting item to datetime object."""

    def _convert_field_item(self, data: str, **kwargs) -> \
            Union['datetime', str]:
        """Actual converting."""

        _format = kwargs.get('format')
        return datetime.strptime(data, _format)


class LinestringField(Field):
    """Converting item to list of integers."""

    def _convert_field_item(self, data: str, **kwargs) -> \
            List[Tuple[float]]:
        """Actual converting."""

        coordinates = []
        for coordinate in data[12:-1].split(','):
            coordinates.append(
                tuple(map(float, coordinate.strip().split(' '))))

        return coordinates
