import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class PS02PS06Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ps02_ps06_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .fleet_vessel_positions()

        self.assertEqual(request.models[0].mmsi, 304010417)
        self.assertEqual(request.models[0].imo, 9015462)
        self.assertEqual(request.models[0].ship_id, 359396)
        self.assertEqual(request.models[0].latitude, 47.758499)
        self.assertEqual(request.models[0].longitude, -5.154223)
        self.assertEqual(request.models[0].speed, 74)
        self.assertEqual(request.models[0].heading, 329)
        self.assertEqual(request.models[0].course, 327)
        self.assertEqual(request.models[0].status, 0)
        self.assertEqual(request.models[0].timestamp, datetime(2017, 5, 19, 9, 39, 57))
        self.assertEqual(request.models[0].dsrc, 'TER')
        self.assertEqual(request.models[0].utc_seconds, 54)
        self.assertEqual(request.models[0].ship_name, 'DORNUM')
        self.assertEqual(request.models[0].ship_type, 70)
        self.assertEqual(request.models[0].call_sign, 'V2OZ')
        self.assertEqual(request.models[0].flag, 'AG')
        self.assertEqual(request.models[0].length, 81.7900009)
        self.assertEqual(request.models[0].width, 11.3000002)
        self.assertEqual(request.models[0].grt, 1662)
        self.assertEqual(request.models[0].dwt, 2369)
        self.assertEqual(request.models[0].year_built, 1993)
        self.assertEqual(request.models[0].rot, 6)
        self.assertEqual(request.models[0].type_name, 'General Cargo')
        self.assertEqual(request.models[0].ais_type_summary, 'Cargo')
        self.assertEqual(request.models[0].current_port, '')
        self.assertEqual(request.models[0].current_port_id, 0)
        self.assertEqual(request.models[0].current_port_unlocode, '')
        self.assertEqual(request.models[0].current_port_country, '')
        self.assertEqual(request.models[0].last_port, 'BILBAO ANCH')
        self.assertEqual(request.models[0].last_port_time, datetime(2017, 5, 16, 15, 37, 0))
        self.assertEqual(request.models[0].destination, 'GREENORE')
        self.assertEqual(request.models[0].eta, datetime(2017, 5, 20, 8, 0, 0))
        self.assertEqual(request.models[0].draught, 44)
        self.assertEqual(request.models[0].last_port_id, 20648)
        self.assertEqual(request.models[0].last_port_unlocode, '')
        self.assertEqual(request.models[0].last_port_country, 'ES')
        self.assertEqual(request.models[0].next_port_id, 251)
        self.assertEqual(request.models[0].next_port_unlocode, 'IEGRN')
        self.assertEqual(request.models[0].next_port_name, 'GREENORE')
        self.assertEqual(request.models[0].next_port_country, 'IE')
        self.assertEqual(request.models[0].eta_calc, datetime(2017, 5, 21, 9, 55, 0))
        self.assertEqual(request.models[0].eta_updated, datetime(2017, 5, 19, 9, 7, 0))
        self.assertEqual(request.models[0].distance_to_go, 407)
        self.assertEqual(request.models[0].distance_travelled, 364)
        self.assertEqual(request.models[0].awg_speed, 8.5)
        self.assertEqual(request.models[0].max_speed, 8.80000019)
