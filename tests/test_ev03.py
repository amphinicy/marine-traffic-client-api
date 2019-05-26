import os
import unittest
from datetime import datetime
from collections import OrderedDict

from marinetrafficapi.client import Client


class EV03Response(unittest.TestCase):

    def setUp(self):
        self._api_key = '_api_key_'
        self.fake_ok_response_path_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'tests', 'responses', 'ev03_response.json'
        )

    def test_ok_response_json(self):
        request = Client(self._api_key,
                         fake_response_path=self.fake_ok_response_path_json) \
            .berth_calls(**OrderedDict([('dwt_min', 2000),
                                        ('dwt_max', 70000),
                                        ('timespan', 20)]))

        url = 'https://services.marinetraffic.com/api/berth-calls/_api_key_/' \
              'msgtype:simple/protocol:jsono/dwt_min:2000/dwt_max:70000/timespan:20'
        self.assertEqual(request.api_reguest.url, url)

        self.assertEqual(request.models[0].ship_id.value, 414650)
        self.assertEqual(request.models[0].mmsi.value, 354530000)
        self.assertEqual(request.models[0].imo.value, 9349813)
        self.assertEqual(request.models[0].dock_local_time.value, datetime(2018, 3, 13, 13, 50, 0))
        self.assertEqual(request.models[0].dock_utc_time.value, datetime(2018, 3, 13, 11, 50, 0))
        self.assertEqual(request.models[0].dock_offset_time.value, 2.0)
        self.assertEqual(request.models[0].undock_local_time.value, '')
        self.assertEqual(request.models[0].undock_utc_time.value, '')
        self.assertEqual(request.models[0].undock_offset_time.value, 0.0)
        self.assertEqual(request.models[0].ship_name.value, 'MSC CARMEN')
        self.assertEqual(request.models[0].type_name.value, 'Container Ship')
        self.assertEqual(request.models[0].grt.value, 50963)
        self.assertEqual(request.models[0].dwt.value, 63359)
        self.assertEqual(request.models[0].flag.value, 'PA')
        self.assertEqual(request.models[0].year_built.value, 2008)
        self.assertEqual(request.models[0].berth_id.value, 6)
        self.assertEqual(request.models[0].berth_name.value, 'Container Terminal')
        self.assertEqual(request.models[0].terminal_id.value, 978)
        self.assertEqual(request.models[0].terminal_name.value, 'Container Terminal')
        self.assertEqual(request.models[0].port_name.value, 'PIRAEUS')
        self.assertEqual(request.models[0].port_id.value, 1)
        self.assertEqual(request.models[0].unlocode.value, 'GRPIR')
        self.assertEqual(request.models[0].country_code.value, None)
        self.assertEqual(request.models[0].destination_id.value, 32)
        self.assertEqual(request.models[0].destination.value, 'PAROS')
        self.assertEqual(request.models[0].arrival_local_time.value, datetime(2018, 3, 13, 13, 43, 0))
        self.assertEqual(request.models[0].arrival_utc_time.value, datetime(2018, 3, 13, 11, 43, 0))
        self.assertEqual(request.models[0].arrival_draught.value, 130)
        self.assertEqual(request.models[0].arrival_load_status.value, 3)
        self.assertEqual(request.models[0].distance_travelled.value, 2931)
        self.assertEqual(request.models[0].voyage_average_speed.value, 188)
        self.assertEqual(request.models[0].voyage_max_speed.value, 226)
        self.assertEqual(request.models[0].voyage_idle_time.value, 7)
        self.assertEqual(request.models[0].origin_name.value, 'ANTWERP')
        self.assertEqual(request.models[0].origin_port_id.value, 117)
        self.assertEqual(request.models[0].origin_departure_time.value, datetime(2018, 3, 7, 5, 36, 0))
        self.assertEqual(request.models[0].total_voyage_time.value, 9007)
        self.assertEqual(request.models[0].departure_local_time.value, '')
        self.assertEqual(request.models[0].departure_utc_time.value, '')
        self.assertEqual(request.models[0].departure_draught.value, 0)
        self.assertEqual(request.models[0].departure_load_status.value, 0)
        self.assertEqual(request.models[0].port_operation.value, 0)
        self.assertEqual(request.models[0].time_at_berth.value, 0)
        self.assertEqual(request.models[0].time_at_port.value, 0)
