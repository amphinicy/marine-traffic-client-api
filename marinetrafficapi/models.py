from datetime import datetime
from typing import Union, List

from marinetrafficapi.paging import Paging


class Model(object):
    """Abstract model class."""

    @classmethod
    def process(cls, data: list) -> Union[object, List[object]]:
        """Transform raw data into models."""

        return [cls(*item) for item in data]

    def convert_bool(self, value: Union['1', '0']) -> bool:
        """Convert 1 or 0 to True or False."""

        if value == '1':
            return True
        else:
            return False

    def convert_linestring(self, data: str) -> Union[None, list]:
        """Convert LINESTRING to list."""

        if not data:
            return None
        return data[12:-1].split(' ')

    """def convert_datetime(self, date_time):
        try:
            dt = date_time.split(' ')
            d = dt[0].split('/')
            t = dt[1].split(':')
            return datetime(int(d[2]), int(d[1]), int(d[0]), int(t[0]), int(t[1]), int(t[2]))
        except:
            return date_time"""


class Route(Model):
    """Receive a list of available routes and distances
    from a specific point to a port or from port to port"""

    def __init__(self, *item):
        self.distance = int(item[0])
        self.panama = self.convert_bool(item[1])
        self.suez = self.convert_bool(item[2])
        self.final_path = self.convert_linestring(item[3] or None)
