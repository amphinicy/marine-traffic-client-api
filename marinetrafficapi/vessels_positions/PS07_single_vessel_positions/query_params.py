from marinetrafficapi.query_params import QueryParams


class PS07QueryParams(QueryParams):
    """Query params for PS02 API call."""

    time_span = 'timespan', 'The maximum age, in minutes, of the returned positions. \n' \
                            'Maximum value for terrestrial coverage is 60. \n' \
                            'Maximum value for satellite coverage is 180.'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by MarineTraffic for the subject vessel'
