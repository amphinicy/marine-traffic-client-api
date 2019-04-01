import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class EV02Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ev02_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .vessel_events(mmsi=355906000,
                           event_type=19,
                           timespan=160)

        url = 'https://services.marinetraffic.com/api/vesselevents/_api_key_/' \
              'msgtype:simple/protocol:jsono/mmsi:355906000/event_type:19/timespan:160'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].mmsi, 355906000)
        self.assertEqual(request.models[0].ship_name, "MSC OSCAR")
        self.assertEqual(request.models[0].timestamp, datetime(2016, 4, 10, 12, 2, 0))
        self.assertEqual(request.models[0].event_id, 2)
        self.assertEqual(request.models[0].event_name, 'INTERMEDIATE_DAILY_POS')
        self.assertEqual(request.models[0].event_content, 'At Lat:35.9598 / Lon:-6.02252')
