import os
import unittest

from marinetrafficapi.client import Client


class VI06Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'vi06_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .port_congestion(year=2018,
                             market='wet bulk',
                             ship_class='handysize',
                             week=15,
                             port_id=1)

        query = [tuple(q.split(':')) for q in
                 sorted(request.api_reguest.url.split(
                     'https://services.marinetraffic.com/api/port-congestion/_api_key_/'
                 )[1].split('/'))]

        test_query = [
            ('market', 'wet bulk'), ('portid', '1'), ('protocol', 'jsono'),
            ('shipclass', 'handysize'), ('week', '15'), ('year', '2018')
        ]

        self.assertEqual(query, test_query)

        self.assertEqual(request.models[0].port_id.value, 1)
        self.assertEqual(request.models[0].year.value, 2018)
        self.assertEqual(request.models[0].week.value, 15)
        self.assertEqual(request.models[0].market.value, 'WET BULK')
        self.assertEqual(request.models[0].ship_class.value, 'HANDYSIZE')
        self.assertEqual(request.models[0].time_anch.value, 0.3)
        self.assertEqual(request.models[0].time_port.value, 0.7)
        self.assertEqual(request.models[0].vessels.value, 17)
        self.assertEqual(request.models[0].calls.value, 33)
        self.assertEqual(request.models[0].time_anch_stdev.value, 1.1)
        self.assertEqual(request.models[0].time_anch_diff.value, 0.1)
        self.assertEqual(request.models[0].time_anch_diff_perc.value, 50.0)
        self.assertEqual(request.models[0].time_port_stdev.value, 9.0)
        self.assertEqual(request.models[0].time_port_diff.value, 0.0)
        self.assertEqual(request.models[0].time_port_diff_perc.value, 0.0)
