from marinetrafficapi.query_params import QueryParams


class EV01QueryParams(QueryParams):
    """Query params for EV01 API call."""

    params = {
        # The maximum age, in minutes, of the returned port calls. Maximum value is 2880.
        'time_span': 'timespan',

        # If used with the value extended,
        # the response includes voyage related data since the previous port call.
        'msg_type': 'msgtype',

        # Response type. Use one of the following: xml, csv, json, jsono (object)
        'protocol': 'protocol',

        # The MarineTraffic ID of the port you wish to monitor (found on the URL
        # of the respective Port page) or port UN/LOCODE.
        'port_id': 'portid',

        # The Maritime Mobile Service Identity (MMSI) of the vessel you wish to track.
        'mmsi': 'mmsi',

        # The International Maritime Organization (IMO) number of the vessel you wish to track.
        'imo': 'imo',

        # A uniquely assigned ID by MarineTraffic for the subject vessel.
        'ship_id': 'shipid',

        # Use 0 to only receive arrivals or 1 to only receive departures.
        # If not used, the response will include both.
        'move_type': 'movetype',

        # Use 1 to exclude vessels in transit
        'exclude_intransit': 'exclude_intransit',

        # Portcalls between fromdate and todate.
        # Date format: YYYY-MM-DD HH:MM
        'from_date': 'fromdate',
        'to_date': 'todate',

        # Data filter: minimum DWT
        # applicable to IMO-having vessels
        'dwt_min': 'dwt_min',

        # Data filter: maximum DWT
        # applicable to IMO-having vessels
        'dwt_max': 'dwt_max',

        # Data filter: minimum GT
        # applicable to IMO-having vessels
        'gt_min': 'gt_min',

        # Data filter: maximum GT
        # applicable to IMO-having vessels
        'gt_max': 'gt_max'
    }
