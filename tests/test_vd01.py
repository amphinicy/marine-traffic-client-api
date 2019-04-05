import os
import unittest

from marinetrafficapi.client import Client


class VD01Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vd01_response.xml'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .vessel_photos(vessel_id=310627000)

        url = 'https://services.marinetraffic.com/api/exportvesselphoto/_api_key_/' \
              'vessel_id:310627000'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].url.value,
                         'https://services.marinetraffic.com/photos/show/864354')
