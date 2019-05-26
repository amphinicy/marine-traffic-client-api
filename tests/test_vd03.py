import os
import unittest

from marinetrafficapi.client import Client


class VD03Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vd03_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .search_vessel(imo=9375783)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/shipsearch/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('imo', '9375783'), ('protocol', 'jsono')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].id.value, 280171)
        self.assertEqual(request.models[0].name.value, 'FOUR SMILE')
        self.assertEqual(request.models[0].mmsi.value, 247271800)
        self.assertEqual(request.models[0].imo.value, 9189146)
        self.assertEqual(request.models[0].call_sign.value, 'IBPQ')
        self.assertEqual(request.models[0].type_name.value, 'Oil Products Tanker')
        self.assertEqual(request.models[0].dwt.value, 160573)
        self.assertEqual(request.models[0].flag.value, 'IT')
        self.assertEqual(request.models[0].country.value, 'Italy')
        self.assertEqual(request.models[0].build_year.value, 2001)
        self.assertEqual(request.models[0].details_page_url.value, 'https://www.marinetraffic.com/en/ais/details/ships/shipid:280171/mmsi:247271800/vessel:280171')
