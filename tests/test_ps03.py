import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class PS03Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ps03_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .dynamic_fleet_vessel_positions()

        self.assertEqual(request.models[1].mmsi, 215819000)
        self.assertEqual(request.models[1].imo, 9034731)
        self.assertEqual(request.models[1].ship_id, 150559)
        self.assertEqual(request.models[1].latitude, 47.926899)
        self.assertEqual(request.models[1].longitude, -5.531450)
        self.assertEqual(request.models[1].speed, 122)
        self.assertEqual(request.models[1].heading, 162)
        self.assertEqual(request.models[1].course, 157)
        self.assertEqual(request.models[1].status, 0)
        self.assertEqual(request.models[1].timestamp, datetime(2017, 5, 19, 9, 44, 27))
        self.assertEqual(request.models[1].dsrc, 'TER')
        self.assertEqual(request.models[1].utc_seconds, 28)
        self.assertEqual(request.models[1].ship_name, 'TOUR MARGAUX')
        self.assertEqual(request.models[1].ship_type, 81)
        self.assertEqual(request.models[1].call_sign, '9HBW8')
        self.assertEqual(request.models[1].flag, 'MT')
        self.assertEqual(request.models[1].length, 113.639999)
        self.assertEqual(request.models[1].width, 17.7000008)
        self.assertEqual(request.models[1].grt, 5499)
        self.assertEqual(request.models[1].dwt, 8674)
        self.assertEqual(request.models[1].draught, 64)
        self.assertEqual(request.models[1].year_built, 1993)
        self.assertEqual(request.models[1].rot, 0)
        self.assertEqual(request.models[1].type_name, 'Oil/Chemical Tanker')
        self.assertEqual(request.models[1].ais_type_summary, 'Tanker')
        self.assertEqual(request.models[1].destination, 'BILBAO')
        self.assertEqual(request.models[1].current_port, '')
        self.assertEqual(request.models[1].current_port_id, 0)
        self.assertEqual(request.models[1].current_port_unlocode, '')
        self.assertEqual(request.models[1].current_port_country, '')
        self.assertEqual(request.models[1].last_port, 'HAMBURG')
        self.assertEqual(request.models[1].last_port_time, datetime(2017, 5, 16, 15, 4, 0))
        self.assertEqual(request.models[1].eta, datetime(2017, 5, 20, 16, 0, 0))
        self.assertEqual(request.models[1].last_port_id, 172)
        self.assertEqual(request.models[1].last_port_unlocode, 'DEHAM')
        self.assertEqual(request.models[1].last_port_country, 'DE')
        self.assertEqual(request.models[1].next_port_id, 1271)
        self.assertEqual(request.models[1].next_port_unlocode, 'ESBIO')
        self.assertEqual(request.models[1].next_port_name, 'BILBAO')
        self.assertEqual(request.models[1].next_port_country, 'ES')
        self.assertEqual(request.models[1].eta_calc, datetime(2017, 5, 20, 11, 27, 0))
        self.assertEqual(request.models[1].eta_updated, datetime(2017, 5, 19, 9, 13, 0))
        self.assertEqual(request.models[1].distance_to_go, 295)
        self.assertEqual(request.models[1].distance_travelled, 782)
        self.assertEqual(request.models[1].awg_speed, 12)
        self.assertEqual(request.models[1].max_speed, 13.3999996)
