from datetime import datetime
from typing import Any, Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from marinetrafficapi.models import Model


class Field:
    """Abstract field class."""

    def __init__(self, index: Union[int, str], desc: str = None):
        self._index = index
        self._desc = desc

        self.data = None

    def convert_item(self, model: 'Model') -> None:
        """Convert item to desired item type"""

        if True:#try:
            self.data = model.item[self._index]
        #except IndexError:
        #    self.data = None
        #except: KeyError:
        #    self.data = None

        if True:#try:
            self.data = self._convert_field_item(self.data)
        #except TypeError:
        #    self.data = None

    def _convert_field_item(self, data: Any) -> Any:
        """Actual converting."""


class NumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data: str) -> int:
        """Actual converting."""

        return int(data)


class RealNumberField(Field):
    """Converting item to integer."""

    def _convert_field_item(self, data: str) -> float:
        """Actual converting."""

        return float(data)


class TextField(Field):
    """Converting item to string."""

    def _convert_field_item(self, data: str) -> str:
        """Actual converting."""

        return str(data)


class BooleanField(Field):
    """Converting item to boolean."""

    def _convert_field_item(self, data: str) -> \
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

    def _convert_field_item(self, data: str) -> \
            Union['datetime', str]:
        """Actual converting."""

        if True:#try:
            dt = data.split(' ')
            d = dt[0].split('/')
            t = dt[1].split(':')
            return datetime(int(d[2]), int(d[1]), int(d[0]),
                            int(t[0]), int(t[1]), int(t[2]))
        #except:
        #    return data


class LinestringField(Field):
    """Converting item to list of integers."""

    def _convert_field_item(self, data: str) -> List[float]:
        """Actual converting."""

        coordinates = []
        for coordinate in data[12:-1].split(','):
            coordinates.append(
                tuple(map(float, coordinate.strip().split(' '))))

        return coordinates
