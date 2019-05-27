import os
import unittest

from marinetrafficapi.client import Client


class VI04Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi04_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .predictive_destinations(imo=8105088,
                                     fromportid=1)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/predictive-destination-areas/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('fromportid', '1'), ('imo', '8105088'), ('protocol', 'jsono')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].imo.value, 8105088)
        self.assertEqual(request.models[0].ship_id.value, 214973)
        self.assertEqual(request.models[0].mmsi.value, 241324000)
        self.assertEqual(request.models[0].ship_id.value, 214973)
        self.assertEqual(request.models[0].ship_class.value, 'HANDYSIZE')
        self.assertEqual(request.models[0].manager.value, 'SEKA 02 MARITIME')
        self.assertEqual(request.models[0].owner.value, 'SEKA 02 MARITIME')
        self.assertEqual(request.models[0].from_port_id.value, 1)
        self.assertEqual(request.models[0].from_port.value, 'PIRAEUS')

        self.assertEqual(request.models[0].next_port_1_id.value, 812)
        self.assertEqual(request.models[0].next_port_1.value, 'KALI LIMENES')
        self.assertEqual(request.models[0].next_port_1_prob.value, 0.563)
        self.assertEqual(request.models[0].next_area_1.value, 'EMED')
        self.assertEqual(request.models[0].next_area_1_prob.value, 0.875)

        self.assertEqual(request.models[0].next_port_2_id.value, 29)
        self.assertEqual(request.models[0].next_port_2.value, 'AGIOI THEODOROI')
        self.assertEqual(request.models[0].next_port_2_prob.value, 0.250)
        self.assertEqual(request.models[0].next_area_2.value, 'EMED')
        self.assertEqual(request.models[0].next_area_2_prob.value, 0.875)

        self.assertEqual(request.models[0].next_port_3_id.value, 17)
        self.assertEqual(request.models[0].next_port_3.value, 'CORINTH CANAL')
        self.assertEqual(request.models[0].next_port_3_prob.value, 0.063)
        self.assertEqual(request.models[0].next_area_3.value, 'EMED')
        self.assertEqual(request.models[0].next_area_3_prob.value, 0.875)

        self.assertEqual(request.models[0].next_port_4_id.value, 2507)
        self.assertEqual(request.models[0].next_port_4.value, 'TRIPOLI')
        self.assertEqual(request.models[0].next_port_4_prob.value, 0.063)
        self.assertEqual(request.models[0].next_area_4.value, 'WMED')
        self.assertEqual(request.models[0].next_area_4_prob.value, 0.063)

        self.assertEqual(request.models[0].next_port_5_id.value, 1688)
        self.assertEqual(request.models[0].next_port_5.value, 'TUZLA')
        self.assertEqual(request.models[0].next_port_5_prob.value, 0.063)
        self.assertEqual(request.models[0].next_area_5.value, 'BSEA')
        self.assertEqual(request.models[0].next_area_5_prob.value, 0.063)
