from marinetrafficapi.query_params import QueryParams


class VI07QueryParams(QueryParams):
    """Query params params for VI07 API call."""

    port_id = 'portid', 'The MarineTraffic ID of the port you wish \n' \
                        'to monitor (found on the URL of the respective \n' \
                        'Port page) or port UN/LOCODE.'

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity \n' \
                   '(MMSI) of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization \n' \
                 '(IMO) number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by \n' \
                        'MarineTraffic for the subject vessel.'

    unlcode = 'unlocode', 'The UN LOCODE (without gaps or spaces) \n' \
                          'of the port you wish to receive ETA info'

    speed_calc = 'speed_calc', 'The Speed of the Vessel that MarineTraffic \n' \
                               'will use to produce the ETA value. If not \n' \
                               'defined the last average speed of the Vessel \n' \
                               'will be used. If no average speed exists \n' \
                               'then a default value of 12(kn) will be used'
