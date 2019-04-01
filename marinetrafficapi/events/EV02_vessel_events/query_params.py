from marinetrafficapi.query_params import QueryParams


class EV02QueryParams(QueryParams):
    """Query params for EV01 API call."""

    params = {
        # The maximum age, in minutes, of the returned port calls. Maximum value is 2880.
        'time_span': 'timespan',

        # If used with the value extended,
        # the response includes voyage related data since the previous port call.
        'msg_type': 'msgtype',

        # Response type. Use one of the following: xml, csv, json, jsono (object)
        'protocol': 'protocol',

        # The Maritime Mobile Service Identity (MMSI) of the vessel you wish to track.
        'mmsi': 'mmsi',

        # The International Maritime Organization (IMO) number of the vessel you wish to track.
        'imo': 'imo',

        # A uniquely assigned ID by MarineTraffic for the subject vessel.
        'ship_id': 'shipid',

        # Portcalls between fromdate and todate.
        # Date format: YYYY-MM-DD HH:MM
        'from_date': 'fromdate',
        'to_date': 'todate',

        # You may use one or more event ids in comma separated format
        # for the events you wish to receive.
        'event_type': 'event_type',

        # Limit the number of results.
        'limit_events': 'limit_events'
    }
