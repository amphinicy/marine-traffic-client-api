import os
import unittest

from marinetrafficapi.client import Client


class TestResponse(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self._base_url = 'https://services.marinetraffic.com/en/api/exportroutes/_api_key_'
        self._url = self._base_url + '/msgtype:extended/protocol:jsono/port_start_id:1/' \
                                     'port_target_id:10/includealternatives:1/includeinland:0'
        self.fake_error_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'errors.json'
        )
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'routes_ok.json'
        )
        self.fake_error_response_path_csv = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'errors.csv'
        )
        self.fake_ok_response_path_csv = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'routes_ok.csv'
        )
        self.fake_error_response_path_xml = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'errors.xml'
        )
        self.fake_ok_response_path_xml = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'routes_ok.xml'
        )
        self._request_params = {
            'port_start_id': 1,
            'port_target_id': 10,
            'include_alternatives': True,
            'include_in_land': False
        }
        self._test_response = [{
                "DISTANCE": "7891",
                "PANAMA": "0",
                "SUEZ": "1",
                "FINAL_PATH": "LINESTRING (23.5935 37.9475, 23.5997 37.9455, "
                              "23.605 37.9413, 122.867 31.0829, 122.308 31.1024, "
                              "122.093 31.228)",
        }]
        self._final_path = [
            (23.5935, 37.9475),
            (23.5997, 37.9455),
            (23.605, 37.9413),
            (122.867, 31.0829),
            (122.308, 31.1024),
            (122.093, 31.228)
        ]

    def test_ok_response_json(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path_json)\
            .port_distances_and_routes(**self._request_params)

        self.assertEqual(request.formatted_data, self._test_response)

        self.assertEqual(request.models[0].distance.value, 7891)
        self.assertFalse(request.models[0].panama.value)
        self.assertTrue(request.models[0].suez.value)
        self.assertEqual(request.models[0].final_path.value, self._final_path)

    def test_ok_response_csv(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path_csv)\
            .port_distances_and_routes(protocol='csv', **self._request_params)

        self.assertEqual(request.formatted_data, self._test_response)

        self.assertEqual(request.models[0].distance.value, 7891)
        self.assertFalse(request.models[0].panama.value)
        self.assertTrue(request.models[0].suez.value)
        self.assertEqual(request.models[0].final_path.value, self._final_path)

    def test_ok_response_xml(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path_xml)\
            .port_distances_and_routes(protocol='xml', **self._request_params)

        self.assertEqual(request.formatted_data, self._test_response)

        self.assertEqual(request.models[0].distance.value, 7891)
        self.assertFalse(request.models[0].panama.value)
        self.assertTrue(request.models[0].suez.value)
        self.assertEqual(request.models[0].final_path.value, self._final_path)

    def test_error_response_json(self):
        with self.assertRaises(Exception) as context:
            Client(
                self._api_key,
                fake_response_path=self.fake_error_response_path_json)\
                .port_distances_and_routes(**self._request_params)

        self.assertTrue('Request errors: code 12: TEST ERROR' in str(context.exception))

    def test_error_response_csv(self):
        with self.assertRaises(Exception) as context:
            Client(
                self._api_key,
                fake_response_path=self.fake_error_response_path_csv)\
                .port_distances_and_routes(protocol='csv', **self._request_params)

        self.assertTrue('Request errors: code 12: TEST ERROR' in str(context.exception))

    def test_error_response_xml(self):
        with self.assertRaises(Exception) as context:
            Client(
                self._api_key,
                fake_response_path=self.fake_error_response_path_xml)\
                .port_distances_and_routes(protocol='xml', **self._request_params)

        self.assertTrue('Request errors: code 12: TEST ERROR' in str(context.exception))
