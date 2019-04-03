from marinetrafficapi.query_params import QueryParams


class VI03QueryParams(QueryParams):
    """Query params params for VI03 API call."""

    port_start_id = 'port_start_id', 'The MarineTraffic ID of the port you wish to \n' \
                                     'put as starting point (found on the URL of the \n' \
                                     'respective Port page) or port UN/LOCODE.'

    latitude = 'LAT', 'The latitude of the starting point'

    longitude = 'LON', 'The longitude of the starting point'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    port_target_id = 'port_target_id', 'The MarineTraffic ID of the port you wish to \n' \
                                       'put as target port (found on the URL of the \n' \
                                       'respective Port page) or port UN/LOCODE.'

    include_alternatives = 'includealternatives', 'Use 1 to search for all available routes \n' \
                                                  'regarding the specific journey or 0 to not \n' \
                                                  'include alternative routes'

    include_in_land = 'includeinland', 'Use 1 in order to receive routes which include \n' \
                                       'inland waterways or 0 to not include alternative routes'
