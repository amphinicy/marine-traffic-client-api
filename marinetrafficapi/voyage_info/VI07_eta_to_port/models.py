from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, DatetimeField, \
    RealNumberField


class EtaToPort(Model):
    """Get ETA and voyage information for a
    vessel of your choice, to any port you define"""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - \n"
                            "a nine-digit number sent in digital \n"
                            "form over a radio frequency that identifies \n"
                            "the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation \n"
                           "number - a seven-digit number that \n"
                           "uniquely identifies vessels")

    ship_id = NumberField(index='SHIP_ID',
                          desc="A uniquely assigned ID by \n"
                               "MarineTraffic for the subject vessel")

    last_port = TextField(index='LAST_PORT',
                          desc="The Name of the Last Port \n"
                               "the vessel has visited")

    last_port_time = DatetimeField(index='LAST_PORT_TIME',
                                   desc="The Date and Time (in UTC) that \n"
                                        "the subject vessel departed from \n"
                                        "the Last Port",
                                   format='%Y-%m-%d %H:%M:%S')

    last_port_id = NumberField(index='LAST_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Last Port")

    last_port_unlocode = TextField(index='LAST_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by \n"
                                        "United Nations for the Last Port")

    next_port_unlocode = TextField(index='NEXT_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by \n"
                                        "United Nations for the Next Port")

    next_port_name = TextField(index='NEXT_PORT_NAME',
                               desc="The Name of the Next Port as \n"
                                    "derived by MarineTraffic based on \n"
                                    "the subject vessel's reported Destination")

    eta_calc = DatetimeField(index='ETA_CALC',
                             desc="The Estimated Time of Arrival to \n"
                                  "Destination of the subject vessel \n"
                                  "according to the MarineTraffic calculations",
                             format='%Y-%m-%d %H:%M:%S')

    distance_to_go = NumberField(index='DISTANCE_TO_GO',
                                 desc="The Remaining Distance (in NM) \n"
                                      "for the subject vessel to reach \n"
                                      "the reported Destination")

    distance_travelled = NumberField(index='DISTANCE_TRAVELLED',
                                     desc="The Distance (in NM) that the \n"
                                          "subject vessel has travelled \n"
                                          "since departing from Last Port")

    speed = NumberField(index='SPEED_CALC',
                        desc="The Speed of the vessel that MarineTraffic \n"
                             "used to produce the ETA_CALC value")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the \n"
                               "subject vessel according to the \n"
                               "AIS transmissions")

    draught_max = NumberField(index='DRAUGHT_MAX',
                              desc="The Maximum Draught that has been \n"
                                   "recorded for the subject vessel")

    load_status_name = TextField(index='LOAD_STATUS_NAME',
                                 desc="The Load Condition of the subject vessel \n"
                                      "(In Ballast, Partially Loaded, Loaded)")

    route = TextField(index='ROUTE',
                      desc="The estimated route of the subject \n"
                           "vessel to destination in WKT format")

    etd_calc = DatetimeField(index='ETD_CALC',
                             desc="The Estimated Time of Departure from a \n"
                                  "Destination of the subject vessel according \n"
                                  "to the MarineTraffic calculations based on \n"
                                  "calculated eta, time at \n"
                                  "anchorage & time at port",
                             format='%Y-%m-%d %H:%M:%S')

    time_anch = RealNumberField(index='TIME_ANCH',
                                desc="The median number of days spent \n"
                                     "at anchorage the previous week")

    time_port = RealNumberField(index='TIME_PORT',
                                desc="The median number of days spent at \n"
                                     "port by the selected market/shipclass")
