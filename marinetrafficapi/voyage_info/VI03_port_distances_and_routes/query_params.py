from marinetrafficapi.query_params import QueryParams


class VI03QueryParams(QueryParams):
    """Query params params for VI03 API call."""

    params = {
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
        'include_in_land': 'includeinland'
    }
