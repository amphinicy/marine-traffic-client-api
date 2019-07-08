import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class VI07Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi07_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .eta_to_port(portid=2036,
                         shipid=292,
                         speed_calc=18.8)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/etatoport/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('portid', '2036'), ('protocol', 'jsono'),
            ('shipid', '292'), ('speed_calc', '18.8')
        ]

        self.assertEqual(query, test_query)

        print(type(request.models[0].last_port_time.value))

        self.assertEqual(request.models[0].ship_id.value, 292)
        self.assertEqual(request.models[0].mmsi.value, 228313800)
        self.assertEqual(request.models[0].imo.value, 9450600)
        self.assertEqual(request.models[0].last_port_id.value, 166)
        self.assertEqual(request.models[0].last_port.value, "CAPE TOWN")
        self.assertEqual(request.models[0].last_port_unlocode.value, "ZACPT")
        self.assertEqual(request.models[0].last_port_time.value, datetime(2018, 12, 8, 8, 13, 1))
        self.assertEqual(request.models[0].next_port_name.value, "ROTTERDAM")
        self.assertEqual(request.models[0].next_port_unlocode.value, "NLRTM")
        self.assertEqual(request.models[0].eta_calc.value, datetime(2018, 12, 26, 11, 48, 2))
        self.assertEqual(request.models[0].distance_travelled.value, 200)
        self.assertEqual(request.models[0].distance_to_go.value, 100)
        self.assertEqual(request.models[0].speed.value, 50)
        self.assertEqual(request.models[0].draught.value, 1234)
        self.assertEqual(request.models[0].draught_max.value, 4321)
        self.assertEqual(request.models[0].load_status_name.value, "test1")
        self.assertEqual(request.models[0].route.value, "test2")
        self.assertEqual(request.models[0].etd_calc.value, datetime(2018, 12, 26, 11, 48, 2))
        self.assertEqual(request.models[0].time_anch.value, 10.10)
        self.assertEqual(request.models[0].time_port.value, 20.20)
