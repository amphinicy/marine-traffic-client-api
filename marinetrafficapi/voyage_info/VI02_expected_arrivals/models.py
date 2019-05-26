from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, DatetimeField, \
    RealNumberField


class ExpectedArrival(Model):
    """Get a voyage forecast for a vessel or your MarineTraffic fleet"""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a \n"
                            "nine-digit number sent in digital form \n"
                            "over a radio frequency that identifies \n"
                            "the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation number - a \n"
                           "seven-digit number that uniquely \n"
                           "identifies vessels")

    longitude = RealNumberField(index='LON',
                                desc="A geographic coordinate that specifies \n"
                                     "the east-west position of the vessel \n"
                                     "on the Earth's surface")

    latitude = RealNumberField(index='LAT',
                               desc="a geographic coordinate that specifies \n"
                                    "the north-south position of the vessel \n"
                                    "on the Earth's surface")

    status = NumberField(index='STATUS',
                         desc="The AIS Navigational Status of the subject \n"
                              "vessel as input by the vessel's crew - more. \n"
                              "There might be discrepancies with the vessel's \n"
                              "detail page when vessel speed is near zero \n"
                              "(0) knots.")

    speed = NumberField(index='SPEED',
                        desc="The speed (in knots x10) that the subject \n"
                             "vessel is reporting according to AIS \n"
                             "transmissions")

    course = NumberField(index='COURSE',
                         desc="The course (in degrees) that the subject \n"
                              "vessel is reporting according to AIS \n"
                              "transmissions")

    port_unlocode = TextField(index='PORT_UNLOCODE',
                              desc="A uniquely assigned ID by United \n"
                                   "Nations for the Current Port")

    current_port = TextField(index='CURRENT_PORT',
                             desc="The name of the Port the subject vessel \n"
                                  "is currently in (NULL if the vessel \n"
                                  "is underway)")

    current_port_country = TextField(index='CURRENT_PORT_COUNTRY',
                                     desc="The Country that the Current \n"
                                          "Port is located at")

    next_port_unlocode = TextField(index='NEXT_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by United \n"
                                        "Nations for the Next Port")

    next_port_id = NumberField(index='NEXT_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Next Port")

    next_port_name = TextField(index='NEXT_PORT_NAME',
                               desc="The Name of the Next Port as derived by \n"
                                    "MarineTraffic based on the subject \n"
                                    "vessel's reported Destination")

    next_port_country = TextField(index='NEXT_PORT_COUNTRY',
                                  desc="The Country that the Next \n"
                                       "Port is located at")

    eta = DatetimeField(index='ETA',
                        desc="The Estimated Time of Arrival to Destination \n"
                             "of the subject vessel according to the \n"
                             "AIS transmissions",
                        format='%Y-%m-%dT%H:%M:%S')

    eta_calc = DatetimeField(index='ETA_CALC',
                             desc="The Estimated Time of Arrival to \n"
                                  "Destination of the subject vessel \n"
                                  "according to the MarineTraffic \n"
                                  "calculations",
                             format='%Y-%m-%dT%H:%M:%S')

    eta_updated = DatetimeField(index='ETA_UPDATED',
                                desc="The date and time (in UTC) that the \n"
                                     "ETA was calculated by MarineTraffic",
                                format='%Y-%m-%dT%H:%M:%S')

    timestamp = DatetimeField(index='TIMESTAMP',
                              desc="The date and time (in UTC) that the \n"
                                   "subject vessel's position was recorded \n"
                                   "by MarineTraffic",
                              format='%Y-%m-%dT%H:%M:%S')

    port_id = NumberField(index='PORT_ID',
                          desc="A uniquely assigned ID by MarineTraffic \n"
                               "for the Current Port")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Shipname of the subject vessel")

    ship_type = NumberField(index='SHIPTYPE',
                            desc="The Shiptype of the subject vessel \n"
                                 "according to AIS transmissions")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    call_sign = TextField(index='CALLSIGN',
                          desc="A uniquely designated identifier for \n"
                               "the vessel's transmitter station")

    flag = TextField(index='FLAG',
                     desc="The flag of the subject vessel according \n"
                          "to AIS transmissions")

    length = RealNumberField(index='LENGTH',
                             desc="The overall Length (in metres) \n"
                                  "of the subject vessel")

    width = RealNumberField(index='WIDTH',
                            desc="The Breadth (in metres) of \n"
                                 "the subject vessel")

    grt = NumberField(index='GRT',
                      desc="Gross Tonnage - unitless measure \n"
                           "that calculates the moulded volume of \n"
                           "all enclosed spaces of a ship")

    dwt = NumberField(index='DWT',
                      desc="Deadweight - a measure (in metric tons) of \n"
                           "how much weight a vessel can safely carry \n"
                           "(excluding the vessel's own weight")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the \n"
                               "subject vessel according to the \n"
                               "AIS transmissions")

    year_built = NumberField(index='YEAR_BUILT',
                             desc="The year that the subject vessel was built")

    last_port = TextField(index='LAST_PORT',
                          desc="The Name of the Last Port \n"
                               "the vessel has visited")

    last_port_time = DatetimeField(index='LAST_PORT_TIME',
                                   desc="The Date and Time (in UTC) that the \n"
                                        "subject vessel departed from the \n"
                                        "Last Port",
                                   format='%Y-%m-%dT%H:%M:%S')

    last_port_id = NumberField(index='LAST_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Last Port")

    last_port_unlocode = TextField(index='LAST_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by \n"
                                        "United Nations for the Last Port")

    last_port_country = TextField(index='LAST_PORT_COUNTRY',
                                  desc="The Country that the Last \n"
                                       "Port is located at")
