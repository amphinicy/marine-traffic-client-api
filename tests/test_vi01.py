import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class VI01Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi01_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .voyage_forecasts(mmsi=355906000)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/voyageforecast/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('mmsi', '355906000'), ('protocol', 'jsono')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].mmsi.value, 355906000)
        self.assertEqual(request.models[0].destination.value, "TANGER MED")
        self.assertEqual(request.models[0].last_port_id.value, 2037)
        self.assertEqual(request.models[0].last_port.value, "ROTTERDAM MAASVLAKTE")
        self.assertEqual(request.models[0].last_port_unlocode.value, "NLMSV")
        self.assertEqual(request.models[0].last_port_time.value, datetime(2016, 4, 19, 3, 11, 0))
        self.assertEqual(request.models[0].next_port_id.value, 1099)
        self.assertEqual(request.models[0].next_port_name.value, "TANGER MED")
        self.assertEqual(request.models[0].next_port_unlocode.value, "MAPTM")
        self.assertEqual(request.models[0].eta.value, datetime(2016, 4, 24, 8, 0, 0))
        self.assertEqual(request.models[0].eta_calc.value, datetime(2016, 4, 25, 1, 50, 0))
        self.assertEqual(request.models[0].distance_travelled.value, 112)
        self.assertEqual(request.models[0].distance_to_go.value, 1367)
        self.assertEqual(request.models[0].speed.value, 103)
        self.assertEqual(request.models[0].draught.value, 106)
        self.assertEqual(request.models[0].draught_max.value, 160)
        self.assertEqual(request.models[0].load_status_name.value, "IN_BALLAST")
        self.assertEqual(request.models[0].route.value, [
            (1.3061, 51.9496),
            (1.3198, 51.9253),
            (1.5319, 51.9358),
            (1.5484, 51.9297),
            (1.5628, 51.9072),
            (1.5685, 51.8651),
            (1.6181, 51.8556),
            (1.7286, 51.8272),
            (1.7608, 51.6416),
            (1.8051, 51.546),
            (1.8844, 51.4768),
            (1.9062, 51.4114),
            (1.7662, 51.2317),
            (1.5251, 51.108),
            (1.4385, 51.0599),
            (1.3317, 51.0018),
            (0.5845, 50.6069),
            (-1.3323, 50.2716),
            (-2.9896, 49.9666),
            (-3.9515, 49.6075),
            (-4.5608, 49.376),
            (-5.7686, 48.8919),
            (-7.0977, 47.3094),
            (-9.2948, 44.3644),
            (-10.0952, 43.2789),
            (-10.1024, 42.2256),
            (-10.0907, 41.1925),
            (-10.0974, 39.8082),
            (-10.0934, 38.716),
            (-9.7988, 37.6639),
            (-9.5553, 36.7994),
            (-9.3081, 36.5738),
            (-8.1363, 36.2893),
            (-6.2082, 35.9012),
            (-5.7619, 35.9011),
            (-5.5676, 35.9165),
            (-5.5384, 35.9225),
            (-5.519, 35.9244),
            (-5.5015, 35.9219),
            (-5.4886, 35.9094),
            (-5.49, 35.9048)
        ])
