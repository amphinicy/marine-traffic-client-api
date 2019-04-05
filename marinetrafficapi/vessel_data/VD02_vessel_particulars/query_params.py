from marinetrafficapi.query_params import QueryParams


class VD02QueryParams(QueryParams):
    """Query params for VD02 API call."""

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity (MMSI) \n' \
                   'of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization (IMO) \n' \
                 'number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by MarineTraffic \n' \
                        'for the subject vessel.'

    time_span = 'timespan', 'The maximum age, in minutes, of the returned positions. \n' \
                            'Maximum value for terrestrial coverage is 60. \n' \
                            'Maximum value for satellite coverage is 180.'

    interval = 'interval', 'The interval parameter can be either minutes or days.'
