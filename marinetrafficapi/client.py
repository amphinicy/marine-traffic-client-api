from marinetrafficapi.models import Route
from marinetrafficapi.bind import bind_request
from marinetrafficapi.exceptions import MarineTrafficRequestApiException


class Client(object):
    """Main API class. Sets all API calls."""

    base_url = 'services.marinetraffic.com/en'
    base_path = '/api'
    protocol = 'https'

    def __init__(self, api_key=None, debug=False):
        if not api_key:
            raise MarineTrafficRequestApiException('API key missing!')

        self.api_key = api_key
        self.debug = debug

    export_routes = bind_request(
        api_path='/exportroutes',
        model=Route,
        query_parameters={
            # The MarineTraffic ID of the port you wish to put as starting point
            # (found on the URL of the respective Port page) or port UN/LOCODE.
            'port_start_id': 'port_start_id',

            # The latitude of the starting point
            'latitude': 'LAT',

            # The longitude of the starting point
            'longitude': 'LON',

            # The Maritime Mobile Service Identity (MMSI) of the vessel you wish to track.
            'mmsi': 'mmsi',

            # The International Maritime Organization (IMO) number of the vessel you wish to track.
            'imo': 'imo',

            # A uniquely assigned ID by MarineTraffic for the subject vessel.
            'ship_id': 'shipid',

            # The MarineTraffic ID of the port you wish to put as target port
            # (found on the URL of the respective Port page) or port UN/LOCODE.
            'port_target_id': 'port_target_id',

            # Use 1 to search for all available routes regarding the specific journey
            # or 0 to not include alternative routes
            'include_alternatives': 'includealternatives',

            # Use 1 in order to receive routes which include inland waterways
            # or 0 to not include alternative routes
            'include_in_land': 'includeinland',

            # If used with the value extended, the response includes also
            # route/waypoints as Linestring Geometry in WKT - Well-Known Text
            'msg_type': 'msgtype',

            # Response type. Use one of the following: xml, csv, json, jsono (object)
            'protocol': 'protocol'
        },
        default_parameters={
            'msgtype': 'extended',
            'protocol': 'json'
        }
    )
