from marinetrafficapi.query_params import QueryParams


class VI05QueryParams(QueryParams):
    """Query params params for VI05 API call."""

    port_id = 'portid', 'The MarineTraffic ID of the port you wish \n' \
                        'to monitor (found on the URL of the respective \n' \
                        'Port page) or port UN/LOCODE.'

    market = 'market', 'Define market for which you would like to receive \n' \
                       'berth calls. If undefined and ship-class is also \n' \
                       'undefined, then return all. If undefined and ship-class \n' \
                       'is defined, return based on ship-class. If defined and \n' \
                       'ship-class is undefined, return all ship-classes \n' \
                       'of the specific market.'

    ship_class = 'shipclass', 'Define ship class for which you \n' \
                              'would like to receive berth calls'

    probability = 'probability', 'Define probability over which you \n' \
                                 'would like to receive probable visits \n' \
                                 '(accepted > 0.3)'
