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
            .fleet_vessel_positions(timespan=10)

        url = 'https://services.marinetraffic.com/api/exportvessels/_api_key_/' \
              'v:8/msgtype:simple/protocol:jsono/timespan:10'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].mmsi.value, 304010417)
        self.assertEqual(request.models[0].imo.value, 9015462)
        self.assertEqual(request.models[0].ship_id.value, 359396)
        self.assertEqual(request.models[0].latitude.value, 47.758499)
        self.assertEqual(request.models[0].longitude.value, -5.154223)
        self.assertEqual(request.models[0].speed.value, 74)
        self.assertEqual(request.models[0].heading.value, 329)
        self.assertEqual(request.models[0].course.value, 327)
        self.assertEqual(request.models[0].status.value, 0)
        self.assertEqual(request.models[0].timestamp.value, datetime(2017, 5, 19, 9, 39, 57))
        self.assertEqual(request.models[0].dsrc.value, 'TER')
        self.assertEqual(request.models[0].utc_seconds.value, 54)
        self.assertEqual(request.models[0].ship_name.value, 'DORNUM')
        self.assertEqual(request.models[0].ship_type.value, 70)
        self.assertEqual(request.models[0].call_sign.value, 'V2OZ')
        self.assertEqual(request.models[0].flag.value, 'AG')
        self.assertEqual(request.models[0].length.value, 81.7900009)
        self.assertEqual(request.models[0].width.value, 11.3000002)
        self.assertEqual(request.models[0].grt.value, 1662)
        self.assertEqual(request.models[0].dwt.value, 2369)
        self.assertEqual(request.models[0].year_built.value, 1993)
        self.assertEqual(request.models[0].rot.value, 6)
        self.assertEqual(request.models[0].type_name.value, 'General Cargo')
        self.assertEqual(request.models[0].ais_type_summary.value, 'Cargo')
        self.assertEqual(request.models[0].current_port.value, '')
        self.assertEqual(request.models[0].current_port_id.value, 0)
        self.assertEqual(request.models[0].current_port_unlocode.value, '')
        self.assertEqual(request.models[0].current_port_country.value, '')
        self.assertEqual(request.models[0].last_port.value, 'BILBAO ANCH')
        self.assertEqual(request.models[0].last_port_time.value, datetime(2017, 5, 16, 15, 37, 0))
        self.assertEqual(request.models[0].destination.value, 'GREENORE')
        self.assertEqual(request.models[0].eta.value, datetime(2017, 5, 20, 8, 0, 0))
        self.assertEqual(request.models[0].draught.value, 44)
        self.assertEqual(request.models[0].last_port_id.value, 20648)
        self.assertEqual(request.models[0].last_port_unlocode.value, '')
        self.assertEqual(request.models[0].last_port_country.value, 'ES')
        self.assertEqual(request.models[0].next_port_id.value, 251)
        self.assertEqual(request.models[0].next_port_unlocode.value, 'IEGRN')
        self.assertEqual(request.models[0].next_port_name.value, 'GREENORE')
        self.assertEqual(request.models[0].next_port_country.value, 'IE')
        self.assertEqual(request.models[0].eta_calc.value, datetime(2017, 5, 21, 9, 55, 0))
        self.assertEqual(request.models[0].eta_updated.value, datetime(2017, 5, 19, 9, 7, 0))
        self.assertEqual(request.models[0].distance_to_go.value, 407)
        self.assertEqual(request.models[0].distance_travelled.value, 364)
        self.assertEqual(request.models[0].awg_speed.value, 8.5)
        self.assertEqual(request.models[0].max_speed.value, 8.80000019)
