import os
import unittest

from marinetrafficapi.client import Client


class VD02Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vd02_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .vessel_particulars(imo=9375783)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/vesselmasterdata/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('imo', '9375783'), ('protocol', 'jsono'), ('v', '3')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].mmsi.value, 304932000)
        self.assertEqual(request.models[0].imo.value, 9375783)
        self.assertEqual(request.models[0].name.value, 'STAPELMOOR')
        self.assertEqual(request.models[0].build_place.value, '')
        self.assertEqual(request.models[0].build_year.value, 2006)
        self.assertEqual(request.models[0].breadth_extreme.value, 12.4)
        self.assertEqual(request.models[0].summer_dwt.value, 2930)
        self.assertEqual(request.models[0].displacement_summer.value, 0)
        self.assertEqual(request.models[0].call_sign.value, 'V2BU8')
        self.assertEqual(request.models[0].flag.value, 'AG')
        self.assertEqual(request.models[0].draught.value, 4.36)
        self.assertEqual(request.models[0].overall_length.value, 88.53)
        self.assertEqual(request.models[0].fuel_consumption.value, '')
        self.assertEqual(request.models[0].max_speed.value, 0)
        self.assertEqual(request.models[0].condition_speed.value, 10.5)
        self.assertEqual(request.models[0].wet_cargo_capacity.value, 0)
        self.assertEqual(request.models[0].owner.value, '')
        self.assertEqual(request.models[0].manager.value, '')
        self.assertEqual(request.models[0].vessel_type.value, 'GENERAL CARGO')
        self.assertEqual(request.models[0].manager_owner.value, 'BOJEN REEDEREI')
