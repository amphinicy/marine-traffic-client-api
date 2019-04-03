import os
import unittest

from marinetrafficapi.client import Client


class VI03Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi03_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .port_distances_and_routes()

        self.assertEqual(request.models[0].distance.value, 7891)
        self.assertFalse(request.models[0].panama.value)
        self.assertTrue(request.models[0].suez.value)
        self.assertEqual(request.models[0].final_path.value, [
            (23.5935, 37.9475),
            (23.5997, 37.9455),
            (23.605, 37.9413),
            (122.867, 31.0829),
            (122.308, 31.1024),
            (122.093, 31.228)
        ])
