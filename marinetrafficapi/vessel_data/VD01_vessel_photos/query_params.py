from marinetrafficapi.query_params import QueryParams


class VD01QueryParams(QueryParams):
    """Query params for VD01 API call."""

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    vessel_id = 'vessel_id', 'The Maritime Mobile Service Identity \n' \
                             '(MMSI) or the IMO number of the vessel.'
