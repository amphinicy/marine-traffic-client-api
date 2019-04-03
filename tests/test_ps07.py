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
            .single_vessel_positions(timespan=20,
                                     mmsi=310627000)

        url = 'https://services.marinetraffic.com/api/exportvessel/_api_key_/' \
              'v:5/msgtype:simple/protocol:jsono/timespan:20/mmsi:310627000'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].mmsi.value, 205623000)
        self.assertEqual(request.models[0].imo.value, 9549645)
        self.assertEqual(request.models[0].latitude.value, 37.24538)
        self.assertEqual(request.models[0].longitude.value, 25.590981)
        self.assertEqual(request.models[0].speed.value, 65)
        self.assertEqual(request.models[0].heading.value, 250)
        self.assertEqual(request.models[0].course.value, 288)
        self.assertEqual(request.models[0].status.value, 0)
        self.assertEqual(request.models[0].timestamp.value, datetime(2016, 4, 18, 19, 21, 0))
        self.assertEqual(request.models[0].dsrc.value, 'SAT')
        self.assertEqual(request.models[0].ship_name.value, 'MALACHITE')
        self.assertEqual(request.models[0].ship_type.value, 70)
        self.assertEqual(request.models[0].call_sign.value, 'ONHL')
        self.assertEqual(request.models[0].flag.value, 'BE')
        self.assertEqual(request.models[0].length.value, 90)
        self.assertEqual(request.models[0].width.value, 14)
        self.assertEqual(request.models[0].grt.value, 3517)
        self.assertEqual(request.models[0].dwt.value, 5000)
        self.assertEqual(request.models[0].year_built.value, 2012)
        self.assertEqual(request.models[0].type_name.value, 'Passengers Ship')
        self.assertEqual(request.models[0].ais_type_summary.value, 'Passenger')
        self.assertEqual(request.models[0].current_port.value, '')
        self.assertEqual(request.models[0].current_port_id.value, 0)
        self.assertEqual(request.models[0].current_port_unlocode.value, '')
        self.assertEqual(request.models[0].last_port.value, 'FREMANTLE')
        self.assertEqual(request.models[0].last_port_time.value, datetime(2016, 4, 16, 18, 26, 0))
        self.assertEqual(request.models[0].destination.value, 'DERINCE')
        self.assertEqual(request.models[0].eta.value, datetime(2017, 4, 20, 14, 0, 0))
        self.assertEqual(request.models[0].draught.value, 50)
        self.assertEqual(request.models[0].last_port_id.value, 768)
        self.assertEqual(request.models[0].last_port_unlocode.value, 'AUFRE')
        self.assertEqual(request.models[0].next_port_id.value, 890)
        self.assertEqual(request.models[0].next_port_unlocode.value, 'AUADL')
        self.assertEqual(request.models[0].next_port_name.value, 'ADELAIDE')
        self.assertEqual(request.models[0].next_port_country.value, 'AU')
        self.assertEqual(request.models[0].eta_calc.value, datetime(2017, 5, 20, 14, 0, 0))
