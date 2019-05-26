from marinetrafficapi.query_params import QueryParams


class VI02QueryParams(QueryParams):
    """Query params params for VI02 API call."""

    time_span = 'timespan', 'Number of days in the future to look for \n' \
                            'expected arrivals, starting from the time the \n' \
                            'API call is requested. Maximum value is 40 days. \n' \
                            'If neither this nor the fromdate/todate \n' \
                            'parameters are used, the response only includes \n' \
                            'vessels currently in port (or the country’s \n' \
                            'ports) and the last vessel\'s signal is \n' \
                            'received during the last 2 days.'

    days_last_signal = 'days_last_signal', \
                       'Include vessels currently in port that \n' \
                       'have transmitted a position within the last \n' \
                       'x days (based on their last signal timestamp). \n' \
                       'This parameter only works when no other ' \
                       'timeframe is defined.'

    from_date = 'fromdate', 'Timestamp in the future to start \n' \
                            'looking for expected arrivals. \n' \
                            'Date format: YYYY-MM-DD HH:MM:SS '

    to_date = 'todate', 'Timestamp in the future to start \n' \
                        'looking for expected arrivals. \n' \
                        'Date format: YYYY-MM-DD HH:MM:SS'

    port_id = 'portid', 'The MarineTraffic ID of the port you wish \n' \
                        'to monitor (found on the URL of the \n' \
                        'respective Port page).'

    country = 'country', 'The Country code of interest. \n' \
                         'Response includes all ports within the Country.'

    from_port_id = 'fromportid', 'The MarineTraffic ID of the previous \n' \
                                 'port (found on the URL of the respective \n' \
                                 'Port page) or previous port UNLOCODE.'

    from_country = 'fromcountry', 'The Country code of interest. \n' \
                                  'Response includes only vessels \n' \
                                  'departed from a selected Country.'

    ship_type = 'shiptype', 'Data filter: Vessel type. \n' \
                            '(2=Fishing / 4=High Speed Craft \n' \
                            '/ 6=Passenger / 7=Cargo / 8=Tanker)'

    dwt_min = 'dwt_min', 'Data filter: minimum DWT Use it to filter \n' \
                         'by size Cargo and Tanker IMO-having vessels \n' \
                         '(shiptype = 7, 8)'

    dwt_max = 'dwt_max', 'Data filter: maximum DWT Use it to filter ' \
                         'by size Cargo and Tanker IMO-having vessels \n' \
                         '(shiptype = 7, 8)'

    gt_min = 'gt_min', 'Data filter: minimum GT \n' \
                       'applicable to IMO-having vessels'

    gt_max = 'gt_max', 'Data filter: maximum GT \n' \
                       'applicable to IMO-having vessels'
