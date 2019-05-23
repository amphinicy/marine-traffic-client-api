from marinetrafficapi.query_params import QueryParams


class VD03SearchVessel(QueryParams):
    """Query params for VD03 API call."""

    mmsi = 'mmsi', 'The Maritime Mobile Service Identity (MMSI) \n' \
                   'of the vessel you wish to track.'

    imo = 'imo', 'The International Maritime Organization (IMO) \n' \
                 'number of the vessel you wish to track.'

    ship_id = 'shipid', 'A uniquely assigned ID by MarineTraffic \n' \
                        'for the subject vessel.'

    ship_name = 'shipname', 'The vessel name (you may also find it at \n' \
                            'https://www.marinetraffic.com/en/ais/index/ships/all)'

    ship_type = 'shiptype', 'Data filter: Vessel type. \n' \
                            '(2=Fishing / 4=High Speed Craft / \n' \
                            '6=Passenger / 7=Cargo / 8=Tanker)'

    type_name_id = 'type_name_id', 'Data filter: Vessel type. \n' \
                                   'Find more information at \n' \
                                   'https://help.marinetraffic.com/hc/en-us/\n' \
                                   'articles/205579997-What-is-the-significance\n' \
                                   '-of-the-AIS-Shiptype-number-'
