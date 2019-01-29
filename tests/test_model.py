import unittest

from marinetrafficapi.models import Route
from marinetrafficapi.client import Client


class TestModel(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self._request = Client(self._api_key).routes(test=True,
                                                     port_start_id=1,
                                                     port_target_id=10,
                                                     include_alternatives=True,
                                                     include_in_land=False)
        response = [
            {
                'DISTANCE': '160',
                'FINAL_PATH': 'LINESTRING (24.4897 35.3824, 24.4909 35.3873, 24.4848 '
                              '35.4067, 24.3001 36.2926, 24.1031 36.8574, 23.7967 37.585, '
                              '23.7483 37.6803, 23.5802 37.9425)',
                'PANAMA': '0',
                'SUEZ': '0'
            }
        ]
        self._model = self._request._process_response(200, response)[0]

    def test_type(self):
        self.assertTrue(isinstance(self._model, Route))

    def test_properties(self):
        self.assertEqual(self._model.distance, 160)
        self.assertFalse(self._model.panama)
        self.assertFalse(self._model.suez)

        final_path = [
            ('24.4897', '35.3824'), ('24.4909', '35.3873'), ('24.4848', '35.4067'),
            ('24.3001', '36.2926'), ('24.1031', '36.8574'), ('23.7967', '37.585'),
            ('23.7483', '37.6803'), ('23.5802', '37.9425')
        ]
        self.assertEqual(self._model.final_path, final_path)
