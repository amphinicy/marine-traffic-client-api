from marinetrafficapi.query_params import QueryParams


class EV01QueryParams(QueryParams):
    """Query params for EV01 API call."""

    time_span = 'timespan', 'The maximum age, in minutes, of the \n' \
                            'returned port calls. Maximum value is 2880.'

    port_id = 'portid', 'The MarineTraffic ID of the port you wish \n' \
                        'to monitor (found on the URL of the respective \n' \
                        'Port page) or port UN/LOCODE.'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    move_type = 'movetype', 'Use 0 to only receive arrivals or 1 to \n' \
                            'only receive departures. If not used, \n' \
                            'the response will include both.'

    exclude_intransit = 'exclude_intransit', 'Use 1 to exclude vessels in transit'

    from_date = 'fromdate', 'Portcalls fromdate. \n' \
                            'Date format: YYYY-MM-DD HH:MM'

    to_date = 'todate', 'Portcalls todate. \n' \
                        'Date format: YYYY-MM-DD HH:MM'

    dwt_min = 'dwt_min', 'Data filter: minimum DWT \n' \
                         'applicable to IMO-having vessels'

    dwt_max = 'dwt_max', 'Data filter: maximum DWT \n' \
                         'applicable to IMO-having vessels'

    gt_min = 'gt_min', 'Data filter: minimum GT \n' \
                       'applicable to IMO-having vessels'

    gt_max = 'gt_max', 'Data filter: maximum GT \n' \
                       'applicable to IMO-having vessels'
