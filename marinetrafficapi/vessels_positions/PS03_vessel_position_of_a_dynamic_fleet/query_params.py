from marinetrafficapi.query_params import QueryParams


class PS03QueryParams(QueryParams):
    """Query params params for PS02 API call."""

    params = {
        # The maximum age, in minutes, of the returned positions.
        # Maximum value for terrestrial coverage is 60.
        # Maximum value for satellite coverage is 180.
        'time_span': 'timespan',

        # Data filter: Vessel type.
        # (2=Fishing / 4=High Speed Craft / 6=Passenger / 7=Cargo / 8=Tanker)
        'ship_type': 'shiptype',
    }
