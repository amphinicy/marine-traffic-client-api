from marinetrafficapi.query_params import QueryParams


class PS01QueryParams(QueryParams):
    """Query params params for PS01 API call."""

    params = {
        # The number of days, starting from the time of request and going backwards,
        # for which the response should look for position data. Maximum value is 190 (days).
        'days': 'days',

        # Date format: YYYY-MM-DD HH:MM:SS. If absent, current date will be selected.
        'date_from': 'fromdate',
        'date_to': 'todate',

        # Possible values:
        # hourly: In order to receive hourly vessel positions
        # daily: In order to receive daily vessel positions
        'period': 'period',

        # Define an area for which you wish to either get all the historical
        # vessels' positions or historical positions for a specific vessel.
        # Important! If you do not define a vessel, the maximum period for
        # which you can look back has a maximum period of one day.
        'min_latitude': 'MINLAT',
        'min_longitude': 'MINLON',
        'max_latitude': 'MAXLAT',
        'max_longitude': 'MAXLON',

        # The Maritime Mobile Service Identity (MMSI) of the vessel you wish to track.
        'mmsi': 'mmsi',

        # The International Maritime Organization (IMO) number of the vessel you wish to track.
        'imo': 'imo',

        # A uniquely assigned ID by MarineTraffic for the subject vessel.
        'ship_id': 'shipid',
    }
