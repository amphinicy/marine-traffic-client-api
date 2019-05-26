import os
import unittest

from marinetrafficapi.client import Client


class TestDescriptions(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ps01_response.json'
        )

        self._request = Client(self._api_key,
                               fake_response_path=self.fake_ok_response_path_json) \
            .vessel_historical_track(period='daily',
                                     days=3,
                                     mmsi=241486000)

    def test_model_property(self):
        desc = "Maritime Mobile Service Identity - \n" \
               "a nine-digit number sent in digital \n" \
               "form over a radio frequency that \n" \
               "identifies the vessel's transmitter station"
        self.assertEqual(self._request.models[0].mmsi.__doc__, desc)
