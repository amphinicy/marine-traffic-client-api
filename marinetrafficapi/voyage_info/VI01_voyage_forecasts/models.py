from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, DatetimeField, \
    LinestringField


class VoyageForecast(Model):
    """Get a voyage forecast for a vessel or your MarineTraffic fleet"""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a nine-digit \n"
                            "number sent in digital form over a radio \n"
                            "frequency that identifies the vessel's \n"
                            "transmitter station")

    speed = NumberField(index='SPEED_CALC',
                        desc="The Speed of the vessel that MarineTraffic \n"
                             "used to produce the ETA_CALC value")

    destination = TextField(index='DESTINATION',
                            desc="The Destination of the subject vessel \n"
                                 "according to the AIS transmissions")

    last_port_id = NumberField(index='LAST_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Last Port")

    last_port = TextField(index='LAST_PORT',
                          desc="The Name of the Last Port the vessel has visited")

    last_port_unlocode = TextField(index='LAST_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by \n"
                                        "United Nations for the Last Port")

    last_port_time = DatetimeField(index='LAST_PORT_TIME',
                                   desc="The Date and Time (in UTC) that the \n"
                                        "subject vessel departed from the Last Port",
                                   format='%Y-%m-%dT%H:%M:%S')

    next_port_id = NumberField(index='NEXT_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Next Port")

    next_port_name = TextField(index='NEXT_PORT_NAME',
                               desc="The Name of the Next Port as derived by \n"
                                    "MarineTraffic based on the subject \n"
                                    "vessel's reported Destination")

    next_port_unlocode = TextField(index='NEXT_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by \n"
                                        "United Nations for the Next Port")

    eta = DatetimeField(index='ETA',
                        desc="The Estimated Time of Arrival to \n"
                             "Destination of the subject vessel \n"
                             "according to the AIS transmissions",
                        format='%Y-%m-%dT%H:%M:%S')

    eta_calc = DatetimeField(index='ETA_CALC',
                             desc="The Estimated Time of Arrival to \n"
                                  "Destination of the subject vessel \n"
                                  "according to the MarineTraffic calculations",
                             format='%Y-%m-%dT%H:%M:%S')

    distance_travelled = NumberField(index='DISTANCE_TRAVELLED',
                                     desc="The Distance (in NM) that the subject \n"
                                          "vessel has travelled since departing \n"
                                          "from Last Port")

    distance_to_go = NumberField(index='DISTANCE_TO_GO',
                                 desc="The Remaining Distance (in NM) for \n"
                                      "the subject vessel to reach the \n"
                                      "reported Destination")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the \n"
                               "subject vessel according to the AIS \n"
                               "transmissions")

    draught_max = NumberField(index='DRAUGHT_MAX',
                              desc="The Maximum Draught that has been \n"
                                   "recorded for the subject vessel")

    load_status_name = TextField(index='LOAD_STATUS_NAME',
                                 desc="The Load Condition of the subject vessel \n"
                                      "(In Ballast, Partially Loaded, Loaded)")

    route = LinestringField(index='ROUTE',
                            desc="The estimated route of the subject \n"
                                 "vessel to destination in WKT format")
