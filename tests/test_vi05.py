import os
import unittest

from marinetrafficapi.client import Client


class VI05Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi05_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .predictive_arrivals(port_id=51)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/predictive-arrivals/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('portid', '51'), ('protocol', 'jsono')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].imo.value, 8817564)
        self.assertEqual(request.models[0].ship_id.value, 213546)
        self.assertEqual(request.models[0].mmsi.value, 240708000)
        self.assertEqual(request.models[0].ship_class.value, 'HANDYSIZE')
        self.assertEqual(request.models[0].ship_name.value, 'AEGEAN III')
        self.assertEqual(request.models[0].market.value, 'WET BULK')

        self.assertEqual(request.models[0].from_port_id.value, 5)
        self.assertEqual(request.models[0].from_port.value, 'ELEFSIS')
        self.assertEqual(request.models[0].next_port_id.value, 51)
        self.assertEqual(request.models[0].next_port.value, 'PATRA')
        self.assertEqual(request.models[0].next_area.value, "EMED")
        self.assertEqual(request.models[0].next_port_prob.value, 0.786)
        self.assertEqual(request.models[0].next_area_prob.value, 1.000)
