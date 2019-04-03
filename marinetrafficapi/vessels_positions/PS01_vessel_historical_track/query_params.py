from marinetrafficapi.query_params import QueryParams


class PS01QueryParams(QueryParams):
    """Query params for PS01 API call."""

    days = 'days', 'The number of days, starting from the time of request \n'\
                   'and going backwards, for which the response should look \n'\
                   'for position data. Maximum value is 190 (days).'

    date_from = 'fromdate', 'From date format: YYYY-MM-DD HH:MM:SS. \n' \
                            'If absent, current date will be selected.'

    date_to = 'todate', 'To date format: YYYY-MM-DD HH:MM:SS. \n' \
                        'If absent, current date will be selected.'

    period = 'period', 'Possible values: \n' \
                       'hourly: In order to receive hourly vessel positions \n' \
                       'daily: In order to receive daily vessel positions'

    min_latitude = 'MINLAT', 'Minimum latitude'

    min_longitude = 'MINLON', 'Minimum longitude'

    max_latitude = 'MAXLAT', 'Maximum latitude'

    max_longitude = 'MAXLON', 'Maximum longitude'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity (MMSI) \n' \
                   'of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization (IMO) \n' \
                 'number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by MarineTraffic \n' \
                        'for the subject vessel.'
