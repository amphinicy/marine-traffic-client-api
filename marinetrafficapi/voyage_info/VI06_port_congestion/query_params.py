from marinetrafficapi.query_params import QueryParams


class VI06QueryParams(QueryParams):
    """Query params params for VI06 API call."""

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

    year = 'year', 'Year of interest (data available back to 1 year). \n' \
                   'Information further back can be requested ad hoc'

    week = 'week', 'Week of Year that is of interest \n' \
                   '(e.g. for week 18/2018 input 18). \n' \
                   'For range of weeks use comma e.g. \n' \
                   'for weeks 30 to 35 (30,35)'

    agg_port = 'agg_port', 'If used, portid should not be in request. \n' \
                           'If agg_port = 1, aggregation result of all \n' \
                           'ports will be returned. If 0 a breakdown of \n' \
                           'ports will be returned. If agg_port = 1 \n' \
                           'agg_market cannot be 1..'

    agg_market = 'agg_market', 'If used, market should not be in request. \n' \
                               'If agg_market = 1, aggregation result of \n' \
                               'all markets will be returned. If 0 a \n' \
                               'breakdown of markets will be returned'

    agg_shipclass = 'agg_shipclass', 'If used, shipclass should not \n' \
                                     'be in request. If agg_shipclass = 1, \n' \
                                     'aggregation result of all classes will \n' \
                                     'be returned. If 0 a breakdown \n' \
                                     'of classes will be returned'

    time_anch = 'time_anch', 'Define market for which you would \n' \
                             'like to receive port congestion. \n' \
                             'If undefined and ship-class is also \n' \
                             'undefined, then figures for ALL \n' \
                             'markets/ship-class.. If undefined and \n' \
                             'ship-class is defined, returns based \n' \
                             'on ship-class for ALL applicable to \n' \
                             'size class markets. If defined and \n' \
                             'ship-class is undefined, returns \n' \
                             'figures for the specific market \n' \
                             '(no size class breakdown)'

    time_port = 'time_port', 'The median number of days spent at \n' \
                             'port by the selected market/shipclass. \n' \
                             'Values indicate in between set to be returned'

    vessels = 'vessels', 'Number of vessels that were used \n' \
                         'in the median calculations. Value of \n' \
                         'parameter indicates greater than relation'

    calls = 'calls', 'Number of individual calls that were \n' \
                     'used in the median calculations \n' \
                     '(e.g. if the same vessel has called \n' \
                     'twice within the same week, it will count \n' \
                     'twice in calls and once in vessels. \n' \
                     'Value of parameter indicates \n' \
                     'greater than relation'

    time_anch_stdev = 'time_anch_stdev', 'The standard deviation of days \n' \
                                         'spent at anchorage the previous week. \n' \
                                         'Values indicate in between set to be \n' \
                                         'returned (time_anch_stdev:0.5,1.5)'

    time_anch_diff = 'time_anch_diff', 'The week-to-week difference of number \n' \
                                       'of days spent at anchorage. Values \n' \
                                       'indicate in between set to be returned'

    time_anch_diff_perc = 'time_anch_diff_perc', 'The week-to-week difference of \n' \
                                                 'number of days spent at anchorage \n' \
                                                 'as a percentage.Values indicate in \n' \
                                                 'between set to be returned'

    time_port_stdev = 'time_port_stdev', 'The standard deviation of days spent \n' \
                                         'at port the previous week. Values \n' \
                                         'indicate in between set to be returned \n' \
                                         '(time_port_stdev:0.5,1.5)'

    time_port_diff = 'time_port_diff', 'The week-to-week difference of number \n' \
                                       'of days spent at port. Values indicate \n' \
                                       'in between set to be returned'
