from datetime import datetime
from typing import Any, Union, List, TYPE_CHECKING, Tuple

from marinetrafficapi.constants import BoolConst, MiscConst

if TYPE_CHECKING:
    from marinetrafficapi.models import Model


class Field:
    """Abstract field class."""

    def __init__(self, index: Union[int, str],
                 desc: str = None, **kwargs):
        self._index = index
        self._kwargs = kwargs

        self.__doc__ = desc
        self.value = None

    def convert_item(self, model: 'Model') -> None:
        """Convert item to desired item type"""

        try:
            self.value = model.item[self._index]
        except IndexError:
            self.value = None
        except KeyError:
            self.value = None

        try:
            if self.value is not None:
                self.value = self._convert_field_item(
                    self.value, **self._kwargs
                )
        except TypeError:
            self.value = None

    def _convert_field_item(self, data: Any, **kwargs) -> Any:
        """Actual converting."""

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


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

        try:
            return float(data)
        except ValueError:
            return 0.0


class TextField(Field):
    """Converting item to string."""

    def _convert_field_item(self, data: str, **kwargs) -> str:
        """Actual converting."""

        try:
            return str(data)
        except ValueError:
            return ''


class BooleanField(Field):
    """Converting item to boolean."""

    def _convert_field_item(self, data: str, **kwargs) -> Union[bool, None]:
        """Actual converting."""

        if data == BoolConst.TRUE:
            return True
        elif data == BoolConst.FALSE:
            return False
        else:
            return None


class DatetimeField(Field):
    """Converting item to datetime object."""

    def _convert_field_item(self, data: str, **kwargs) -> Union['datetime', str]:
        """Actual converting."""

        try:
            _format = kwargs.get(MiscConst.FORMAT)
            return datetime.strptime(data, _format)
        except ValueError:
            return data


class LinestringField(Field):
    """Converting item to list of integers."""

    def _convert_field_item(self, data: str, **kwargs) -> List[Tuple[float]]:
        """Actual converting."""

        coordinates = []
        for coordinate in data[12:-1].split(','):
            coordinates.append(
                tuple(map(float, coordinate.strip().split(' '))))

        return coordinates
