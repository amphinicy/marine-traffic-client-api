from marinetrafficapi.query_params import QueryParams


class VI04QueryParams(QueryParams):
    """Query params params for VI04 API call."""

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    fleet_id = 'fleet_id', 'TThe MarineTraffic ID of the \n' \
                           'fleet you wish to track'

    from_port_id = 'fromportid', 'The MarineTraffic ID of the port \n' \
                                 'you wish to receive a prediction \n' \
                                 '(found on the URL of the \n' \
                                 'respective Port page)'
