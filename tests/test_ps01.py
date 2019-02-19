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
            .vessel_historical_track()

        self.assertEqual(request.models[0].mmsi, 241486000)
        self.assertEqual(request.models[0].status, 0)
        self.assertEqual(request.models[0].speed, 146)
        self.assertEqual(request.models[0].latitude, 34.485870)
        self.assertEqual(request.models[0].longitude, 11.904260)
        self.assertEqual(request.models[0].course, 189)
        self.assertEqual(request.models[0].heading, 190)
        self.assertEqual(request.models[0].timestamp, datetime(2017, 7, 12, 10, 6, 0))
        self.assertEqual(request.models[0].ship_id, 4910653)
        self.assertEqual(request.models[0].wind_angle, 340)
        self.assertEqual(request.models[0].wind_speed, 18)
        self.assertEqual(request.models[0].wind_temp, 12)
