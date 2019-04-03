from marinetrafficapi.query_params import QueryParams


class EV03QueryParams(QueryParams):
    """Query params for EV03 API call."""

    time_span = 'timespan', 'The maximum age, in minutes, of the \n' \
                            'returned port calls. Maximum value is 2880.'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    from_date = 'fromdate', 'Portcalls fromdate. \n' \
                            'Date format: YYYY-MM-DD HH:MM'

    to_date = 'todate', 'Portcalls todate. \n' \
                        'Date format: YYYY-MM-DD HH:MM'

    port_id = 'portid', 'The MarineTraffic ID of the port you wish \n' \
                        'to monitor (found on the URL of the respective Port page).'

    port_unlocode = 'port_unlocode', 'Port UN LOCODE (without gaps or spaces)'

    berth_id = 'berth_id', 'The MarineTraffic ID of the berth you wish \n' \
                           'to monitor (list to be provided upon request).'

    terminal_id = 'terminalid', 'The MarineTraffic ID of the terminal you wish \n' \
                                'to monitor (list to be provided upon request)'

    ship_id = 'shipid', 'The MarineTraffic ID of the vessel you wish \n' \
                        'to monitor found on the URL of the respective Vessel page'

    market = 'market', 'Define market for which you would like to receive \n' \
                       'berth calls. If undefined and ship-class is also \n' \
                       'undefined, then return all. If undefined and ship-class \n' \
                       'is defined, return based on ship-class. If defined and \n' \
                       'ship-class is undefined, return all ship-classes \n' \
                       'of the specific market.'

    ship_class = 'shipclass', 'Define ship class for which you \n' \
                              'would like to receive berth calls'

    dwt_min = 'dwt_min', 'Data filter: minimum DWT Use it to filter by size \n' \
                         'Cargo and Tanker IMO-having vessels (shiptype = 7, 8)'

    dwt_max = 'dwt_max', 'Data filter: maximum DWT Use it to filter by size \n' \
                         'Cargo and Tanker IMO-having vessels (shiptype = 7, 8)'

    gt_min = 'gt_min', 'Data filter: minimum GT applicable to IMO-having vessels'

    gt_max = 'gt_max', 'Data filter: maximum GT applicable to IMO-having vessels'
