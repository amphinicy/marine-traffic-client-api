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
            .port_calls(portid=1,
                        gt_min=4000,
                        dwt_min=9000,
                        timespan=60)

        query = [tuple(q.split(':')) for q in sorted(request.api_reguest.url.split(
            'https://services.marinetraffic.com/api/portcalls/_api_key_/'
        )[1].split('/'))]

        test_query = [
            ('dwt_min', '9000'), ('gt_min', '4000'), ('msgtype', 'simple'),
            ('portid', '1'), ('protocol', 'jsono'), ('timespan', '60'),
            ('v', '4')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].mmsi.value, 566312000)
        self.assertEqual(request.models[0].ship_name.value, "MARITIME KELLY ANNE")
        self.assertEqual(request.models[0].ship_id.value, 708694)
        self.assertEqual(request.models[0].local_timestamp.value, datetime(2016, 3, 3, 7, 10, 0))
        self.assertEqual(request.models[0].utc_timestamp.value, datetime(2016, 3, 3, 12, 10, 0))
        self.assertEqual(request.models[0].move_type.value, True)
        self.assertEqual(request.models[0].type_name.value, 'Container Ship')
        self.assertEqual(request.models[0].unlocode.value, 'USMSY')
        self.assertEqual(request.models[0].draught.value, 45)
        self.assertEqual(request.models[0].load_status.value, 0)
        self.assertEqual(request.models[0].port_operation.value, 0)
        self.assertEqual(request.models[0].in_transit.value, False)
        self.assertEqual(request.models[0].voyage_avg_speed.value, 57)
        self.assertEqual(request.models[0].voyage_max_speed.value, 73)
        self.assertEqual(request.models[0].voyage_idle_time.value, 0)
        self.assertEqual(request.models[0].elapsed_noanch.value, 11)
