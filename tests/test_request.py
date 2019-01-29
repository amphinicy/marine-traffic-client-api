import unittest

from marinetrafficapi.client import Client


class TestRequest(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self._request = Client(self._api_key).routes(test=True,
                                                     port_start_id=1,
                                                     port_target_id=10,
                                                     include_alternatives=True,
                                                     include_in_land=False)

    def test_set_parameters(self):
        parameters = {
            'query': {
                'msgtype': 'extended',
                'protocol': 'jsono',
                'port_start_id': 1,
                'port_target_id': 10,
                'includealternatives': '1',
                'includeinland': '0'
            },
            'path': []
        }
        self.assertEqual(self._request.parameters, parameters)

    def test_prepare_request(self):
        url = 'https://services.marinetraffic.com/en/api/exportroutes/_api_key_/msgtype:extended/protocol:jsono/port_start_id:1/port_target_id:10/includealternatives:1/includeinland:0'
        self.assertEqual(self._request._prepare_url(), url)

    def test_errors(self):
        response = {
            'errors': [
                {
                    'code': '12',
                    'detail': 'TEST ERROR'
                }
            ]
        }

        with self.assertRaises(Exception) as context:
            self._request._process_response(200, response)

        self.assertTrue('Request errors: code 12: TEST ERROR' in str(context.exception))
