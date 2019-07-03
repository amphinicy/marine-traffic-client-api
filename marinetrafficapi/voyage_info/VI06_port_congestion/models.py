from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, RealNumberField


class PortCongestion(Model):
    """Receive the Port Congestion for a specific period of time"""

    port_id = NumberField(index='PORT_ID',
                          desc="A uniquely assigned ID by \n"
                               "MarineTraffic for the Current Port")

    year = NumberField(index='YEAR',
                       desc="Year of week the data are referring to")

    week = NumberField(index='WEEK',
                       desc="Week of year the data are referring to")

    market = TextField(index='MARKET',
                       desc="The commercial market segment \n"
                            "the subject vessel belongs to")

    ship_class = TextField(index='SHIPCLASS',
                           desc="The class of the subject vessel \n"
                                "based on vessel type and size")

    time_anch = RealNumberField(index='TIME_ANCH',
                                desc="The median number of days spent \n"
                                     "at anchorage the previous week")

    time_port = RealNumberField(index='TIME_PORT',
                                desc="The median number of days spent at \n"
                                     "port by the selected market/shipclass")

    vessels = NumberField(index='VESSELS',
                          desc="Number of vessels that were \n"
                               "used in the median calculations")

    calls = NumberField(index='CALLS',
                        desc="Number of individual calls that \n"
                             "were used in the median calculations \n"
                             "(e.g. if the same vessel has called \n"
                             "twice within the same week, it will \n"
                             "count twice in CALLS and once in VESSELS")

    time_anch_stdev = RealNumberField(index='TIME_ANCH_STDEV',
                                      desc="The week-to-week standard deviation \n"
                                           "in days spent at anchorage")

    time_anch_diff = RealNumberField(index='TIME_ANCH_DIFF',
                                     desc="The week-to-week difference of \n"
                                          "number of days spent at anchorage")

    time_anch_diff_perc = RealNumberField(index='TIME_ANCH_DIFF_PERC',
                                          desc="The week-to-week difference of \n"
                                               "number of days spent at \n"
                                               "anchorage as a percentage")

    time_port_stdev = RealNumberField(index='TIME_PORT_STDEV',
                                      desc="The week-to-week standard \n"
                                           "deviation in days spent at port")

    time_port_diff = RealNumberField(index='TIME_PORT_DIFF',
                                     desc="The week-to-week difference \n"
                                          "of number of days spent at port")

    time_port_diff_perc = RealNumberField(index='TIME_PORT_DIFF_PERC',
                                          desc="The week-to-week difference \n"
                                               "of number of days spent at \n"
                                               "port as a percentage")
