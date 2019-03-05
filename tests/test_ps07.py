import os
import unittest
from datetime import datetime

from marinetrafficapi.client import Client


class PS07Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ps07_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json)\
            .single_vessel_positions()

        self.assertEqual(request.models[0].mmsi, 205623000)
        self.assertEqual(request.models[0].imo, 9549645)
        self.assertEqual(request.models[0].latitude, 37.24538)
        self.assertEqual(request.models[0].longitude, 25.590981)
        self.assertEqual(request.models[0].speed, 65)
        self.assertEqual(request.models[0].heading, 250)
        self.assertEqual(request.models[0].course, 288)
        self.assertEqual(request.models[0].status, 0)
        self.assertEqual(request.models[0].timestamp, datetime(2016, 4, 18, 19, 21, 0))
        self.assertEqual(request.models[0].dsrc, 'SAT')
        self.assertEqual(request.models[0].ship_name, 'MALACHITE')
        self.assertEqual(request.models[0].ship_type, 70)
        self.assertEqual(request.models[0].call_sign, 'ONHL')
        self.assertEqual(request.models[0].flag, 'BE')
        self.assertEqual(request.models[0].length, 90)
        self.assertEqual(request.models[0].width, 14)
        self.assertEqual(request.models[0].grt, 3517)
        self.assertEqual(request.models[0].dwt, 5000)
        self.assertEqual(request.models[0].year_built, 2012)
        self.assertEqual(request.models[0].type_name, 'Passengers Ship')
        self.assertEqual(request.models[0].ais_type_summary, 'Passenger')
        self.assertEqual(request.models[0].current_port, '')
        self.assertEqual(request.models[0].current_port_id, 0)
        self.assertEqual(request.models[0].current_port_unlocode, '')
        self.assertEqual(request.models[0].last_port, 'FREMANTLE')
        self.assertEqual(request.models[0].last_port_time, datetime(2016, 4, 16, 18, 26, 0))
        self.assertEqual(request.models[0].destination, 'DERINCE')
        self.assertEqual(request.models[0].eta, datetime(2017, 4, 20, 14, 0, 0))
        self.assertEqual(request.models[0].draught, 50)
        self.assertEqual(request.models[0].last_port_id, 768)
        self.assertEqual(request.models[0].last_port_unlocode, 'AUFRE')
        self.assertEqual(request.models[0].next_port_id, 890)
        self.assertEqual(request.models[0].next_port_unlocode, 'AUADL')
        self.assertEqual(request.models[0].next_port_name, 'ADELAIDE')
        self.assertEqual(request.models[0].next_port_country, 'AU')
        self.assertEqual(request.models[0].eta_calc, datetime(2017, 5, 20, 14, 0, 0))
