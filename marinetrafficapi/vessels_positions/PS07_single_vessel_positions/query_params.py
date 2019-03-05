from marinetrafficapi.query_params import QueryParams


class PS07QueryParams(QueryParams):
    """Query params for PS02 API call."""

    params = {
        # The maximum age, in minutes, of the returned positions.
        # Maximum value for terrestrial coverage is 60.
        # Maximum value for satellite coverage is 180.
        'time_span': 'timespan',

        # The Maritime Mobile Service Identity (MMSI) of the vessel you wish to track.
        'mmsi': 'mmsi',

        # The International Maritime Organization (IMO) number of the vessel you wish to track.
        'imo': 'imo',

        # A uniquely assigned ID by MarineTraffic for the subject vessel
        'shipid': 'shipid'
    }
