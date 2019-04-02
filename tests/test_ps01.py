import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class PS01Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ps01_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .vessel_historical_track(period='daily',
                                     days=3,
                                     mmsi=241486000)

        url = 'https://services.marinetraffic.com/api/exportvesseltrack/_api_key_/' \
              'v:2/msgtype:simple/protocol:jsono/period:daily/days:3/mmsi:241486000'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].mmsi.value, 241486000)
        self.assertEqual(request.models[0].status.value, 0)
        self.assertEqual(request.models[0].speed.value, 146)
        self.assertEqual(request.models[0].latitude.value, 34.485870)
        self.assertEqual(request.models[0].longitude.value, 11.904260)
        self.assertEqual(request.models[0].course.value, 189)
        self.assertEqual(request.models[0].heading.value, 190)
        self.assertEqual(request.models[0].timestamp.value, datetime(2017, 7, 12, 10, 6, 0))
        self.assertEqual(request.models[0].ship_id.value, 4910653)
        self.assertEqual(request.models[0].wind_angle.value, 340)
        self.assertEqual(request.models[0].wind_speed.value, 18)
        self.assertEqual(request.models[0].wind_temp.value, 12)
