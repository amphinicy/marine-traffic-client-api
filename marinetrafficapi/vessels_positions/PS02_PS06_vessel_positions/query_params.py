from marinetrafficapi.query_params import QueryParams


class PS02PS06QueryParams(QueryParams):
    """Query params for PS02 API call."""

    time_span = 'timespan', 'The maximum age, in minutes, of the returned positions. \n' \
                            'Maximum value for terrestrial coverage is 60. \n' \
                            'Maximum value for satellite coverage is 180.'

    ship_type = 'shiptype', 'Data filter: Vessel type. (2=Fishing / \n' \
                            '4=High Speed Craft / 6=Passenger / 7=Cargo / 8=Tanker)'

    min_latitude = 'MINLAT', 'Minimum latitude'

    max_latitude = 'MAXLAT', 'Maximum latitude'

    min_longitude = 'MINLON', 'Minimum longitude'

    max_longitude = 'MAXLON', 'Maximim longitude'
