import os
import unittest

from marinetrafficapi.client import Client


class TestRequest(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self._base_url = 'https://services.marinetraffic.com/api/exportroutes/_api_key_/'
        self._url = self._base_url + 'protocol:jsono/port_start_id:1/' \
                                     'port_target_id:10/includealternatives:1/includeinland:0'
        self.fake_ok_response_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'routes_ok.json'
        )
        self._request_params = {
            'port_start_id': 1,
            'port_target_id': 10,
            'include_alternatives': True,
            'include_in_land': False,
            'timeout': 10
        }

    def test_set_parameters(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path)\
            .port_distances_and_routes(*['foo', 'bar'], **self._request_params)

        parameters = {
            'query': {
                'protocol': 'jsono',
                'port_start_id': 1,
                'port_target_id': 10,
                'includealternatives': '1',
                'includeinland': '0'
            },
            'path': ['foo', 'bar']
        }

        #self.assertEqual(request.api_reguest.parameters, parameters)
        self.assertEqual(request.api_reguest._timeout, 10)

    def test_prepare_url(self):
        request = Client(
            self._api_key,
            fake_response_path=self.fake_ok_response_path)\
            .port_distances_and_routes(**self._request_params)

        query = [
            tuple(q.split(':')) for q in sorted(
                request.api_reguest.url.split(self._base_url)[1].split('/')
            )
        ]

        test_query = [
            ('includealternatives', '1'), ('includeinland', '0'),
            ('port_start_id', '1'), ('port_target_id', '10'),
            ('protocol', 'jsono')
        ]

        self.assertEqual(query, test_query)
