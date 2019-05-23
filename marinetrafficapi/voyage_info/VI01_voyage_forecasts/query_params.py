from marinetrafficapi.query_params import QueryParams


class VI01QueryParams(QueryParams):
    """Query params params for VI01 API call."""

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity (MMSI) \n' \
                   'of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization (IMO) \n' \
                 'number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by MarineTraffic \n' \
                        'for the subject vessel.'

    fleet_id = 'fleet_id', 'The fleet id you wish to receive voyage forecast for'
