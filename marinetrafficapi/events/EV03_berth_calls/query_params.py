from marinetrafficapi.query_params import QueryParams


class EV03QueryParams(QueryParams):
    """Query params for EV03 API call."""

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

        # Portcalls between fromdate and todate.
        # Date format: YYYY-MM-DD HH:MM
        'from_date': 'fromdate',
        'to_date': 'todate',

        # The MarineTraffic ID of the port you wish to monitor
        # (found on the URL of the respective Port page).
        'port_id': 'portid',

        # Port UN LOCODE (without gaps or spaces)
        'port_unlocode': 'port_unlocode',

        # The MarineTraffic ID of the berth you wish to monitor
        # (list to be provided upon request).
        'berth_id': 'berth_id',

        # The MarineTraffic ID of the terminal you wish to monitor
        # (list to be provided upon request)
        'terminal_id': 'terminalid',

        # The MarineTraffic ID of the vessel you wish to monitor
        # found on the URL of the respective Vessel page
        'ship_id': 'shipid',

        # Define market for which you would like to receive berth calls.
        # If undefined and ship-class is also undefined, then return all.
        # If undefined and ship-class is defined, return based on ship-class.
        # If defined and ship-class is undefined, return all ship-classes of the specific market.
        'market': 'market',

        # Define ship class for which you would like to receive berth calls
        'ship_class': 'shipclass',

        # Data filter: minimum DWT
        # Use it to filter by size Cargo and Tanker IMO-having vessels (shiptype = 7, 8)
        'dwt_min': 'dwt_min',

        # Data filter: maximum DWT
        # Use it to filter by size Cargo and Tanker IMO-having vessels (shiptype = 7, 8)
        'dwt_max': 'dwt_max',

        # Data filter: minimum GT
        # applicable to IMO-having vessels
        'gt_min': 'gt_max',

        # Data filter: maximum GT
        # applicable to IMO-having vessels
        'gt_max': 'gt_max'
    }
