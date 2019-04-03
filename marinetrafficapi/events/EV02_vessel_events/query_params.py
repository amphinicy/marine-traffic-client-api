from marinetrafficapi.query_params import QueryParams


class EV02QueryParams(QueryParams):
    """Query params for EV02 API call."""

    time_span = 'timespan', 'The maximum age, in minutes, of the \n' \
                            'returned port calls. Maximum value is 2880.'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    from_date = 'fromdate', 'Portcalls fromdate. \n' \
                            'Date format: YYYY-MM-DD HH:MM'

    to_date = 'todate', 'Portcalls todate. \n' \
                        'Date format: YYYY-MM-DD HH:MM'

    event_type = 'event_type', 'You may use one or more event ids in \n' \
                               'comma separated format for the events \n' \
                               'you wish to receive.'

    limit_events = 'limit_events', 'Limit the number of results'

