import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class EV01Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ev01_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .port_calls()

        self.assertEqual(request.models[0].mmsi, 566312000)
        self.assertEqual(request.models[0].ship_name, "MARITIME KELLY ANNE")
        self.assertEqual(request.models[0].ship_id, 708694)
        self.assertEqual(request.models[0].local_timestamp, datetime(2016, 3, 3, 7, 10, 0))
        self.assertEqual(request.models[0].utc_timestamp, datetime(2016, 3, 3, 12, 10, 0))
        self.assertEqual(request.models[0].move_type, True)
        self.assertEqual(request.models[0].type_name, 'Container Ship')
        self.assertEqual(request.models[0].unlocode, 'USMSY')
        self.assertEqual(request.models[0].draught, 45)
        self.assertEqual(request.models[0].load_status, 0)
        self.assertEqual(request.models[0].port_operation, 0)
        self.assertEqual(request.models[0].in_transit, False)
        self.assertEqual(request.models[0].voyage_avg_speed, 57)
        self.assertEqual(request.models[0].voyage_max_speed, 73)
        self.assertEqual(request.models[0].voyage_idle_time, 0)
        self.assertEqual(request.models[0].elapsed_noanch, 11)
