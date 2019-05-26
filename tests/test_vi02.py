import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class VI02Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi02_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .expected_arrivals(timespan=2,
                               country='US',
                               dwt_min=10000,
                               dwt_max=160000,
                               shiptype=7)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/expectedarrivals/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('country', 'US'), ('dwt_max', '160000'), ('dwt_min', '10000'),
            ('protocol', 'jsono'), ('shiptype', '7'), ('timespan', '2'),
            ('v', '3')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].imo.value, 7350325)
        self.assertEqual(request.models[0].mmsi.value, 239308000)
        self.assertEqual(request.models[0].ship_name.value, 'IONIS')
        self.assertEqual(request.models[0].type_name.value, 'Ro-Ro/Passenger Ship')
        self.assertEqual(request.models[0].ship_type.value, 71)
        self.assertEqual(request.models[0].call_sign.value, 'SVKU')
        self.assertEqual(request.models[0].flag.value, 'GR')
        self.assertEqual(request.models[0].length.value, 96)
        self.assertEqual(request.models[0].width.value, 17)
        self.assertEqual(request.models[0].draught.value, 44)
        self.assertEqual(request.models[0].grt.value, 2604)
        self.assertEqual(request.models[0].dwt.value, 880)
        self.assertEqual(request.models[0].year_built.value, 1977)
        self.assertEqual(request.models[0].latitude.value, 37.914780)
        self.assertEqual(request.models[0].longitude.value, 23.604830)
        self.assertEqual(request.models[0].speed.value, 164)
        self.assertEqual(request.models[0].course.value, 63)
        self.assertEqual(request.models[0].status.value, 0)
        self.assertEqual(request.models[0].eta.value, datetime(2016, 10, 20, 10, 36, 0))
        self.assertEqual(request.models[0].eta_calc.value, '')
        self.assertEqual(request.models[0].eta_updated.value, '')
        self.assertEqual(request.models[0].last_port_id.value, 6)
        self.assertEqual(request.models[0].last_port.value, 'AEGINA')
        self.assertEqual(request.models[0].last_port_unlocode.value, 'GRAEG')
        self.assertEqual(request.models[0].last_port_country.value, 'GR')
        self.assertEqual(request.models[0].last_port_time.value, datetime(2016, 10, 19, 13, 6, 0))
        self.assertEqual(request.models[0].port_id.value, 0)
        self.assertEqual(request.models[0].port_unlocode.value, '')
        self.assertEqual(request.models[0].current_port.value, '')
        self.assertEqual(request.models[0].current_port_country.value, '')
        self.assertEqual(request.models[0].next_port_id.value, 1)
        self.assertEqual(request.models[0].next_port_unlocode.value, 'GRPIR')
        self.assertEqual(request.models[0].next_port_name.value, 'PIRAEUS')
        self.assertEqual(request.models[0].next_port_country.value, 'GR')
        self.assertEqual(request.models[0].timestamp.value, datetime(2016, 10, 19, 14, 3, 8))
