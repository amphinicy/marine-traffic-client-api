from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, RealNumberField, DatetimeField, TextField


class SingleVesselPosition(Model):
    """Get positional information for a set of predefined vessels."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a nine-digit number "
                            "sent in digital form over a radio frequency that identifies "
                            "the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation number - a "
                           "seven-digit number that uniquely identifies vessels")

    longitude = RealNumberField(index='LON',
                                desc="A geographic coordinate that specifies the "
                                     "east-west position of the vessel on the "
                                     "Earth's surface")

    latitude = RealNumberField(index='LAT',
                               desc="a geographic coordinate that specifies the "
                                    "north-south position of the vessel on the "
                                    "Earth's surface")

    speed = NumberField(index='SPEED',
                        desc="The speed (in knots x10) that the subject vessel is "
                             "reporting according to AIS transmissions")

    heading = NumberField(index='HEADING',
                          desc="The heading (in degrees) that the subject vessel is "
                               "reporting according to AIS transmissions")

    status = NumberField(index='STATUS',
                         desc="The AIS Navigational Status of the subject vessel as "
                              "input by the vessel's crew - more. There might be "
                              "discrepancies with the vessel's detail page when vessel "
                              "speed is near zero (0) knots.")

    course = NumberField(index='COURSE',
                         desc="The course (in degrees) that the subject vessel is "
                              "reporting according to AIS transmissions")

    timestamp = DatetimeField(index='TIMESTAMP',
                              desc="The date and time (in UTC) that the subject vessel's "
                                   "position was recorded by MarineTraffic",
                              format='%Y-%m-%dT%H:%M:%S')

    dsrc = TextField(index='DSRC',
                     desc="Data Source - Defines whether the transmitted AIS data was "
                          "received by a Terrestrial or a Satellite AIS Station")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    ship_type = NumberField(index='SHIPTYPE',
                            desc="The Ship type of the subject vessel "
                                 "according to AIS transmissions")

    call_sign = TextField(index='CALLSIGN',
                          desc="A uniquely designated identifier for "
                               "the vessel's transmitter station")

    flag = TextField(index='FLAG',
                     desc="The flag of the subject vessel according to AIS transmissions")

    length = RealNumberField(index='LENGTH',
                             desc="The overall Length (in metres) of the subject vessel")

    width = RealNumberField(index='WIDTH',
                            desc="The Breadth (in metres) of the subject vessel")

    grt = NumberField(index='GRT',
                      desc="Gross Tonnage - unitless measure that calculates the "
                           "moulded volume of all enclosed spaces of a ship")

    dwt = NumberField(index='DWT',
                      desc="Deadweight - a measure (in metric tons) of how much weight a "
                           "vessel can safely carry (excluding the vessel's own weight")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the subject vessel "
                               "according to the AIS transmissions")

    year_built = NumberField(index='YEAR_BUILT',
                             desc="The year that the subject vessel was built")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    ais_type_summary = TextField(index='AIS_TYPE_SUMMARY',
                                 desc="Further explanation of the SHIPTYPE ID")

    destination = TextField(index='DESTINATION',
                            desc="The Destination of the subject vessel "
                                 "according to the AIS transmissions")

    eta = DatetimeField(index='ETA',
                        desc="The Estimated Time of Arrival to Destination of the "
                             "subject vessel according to the AIS transmissions",
                        format='%Y-%m-%dT%H:%M:%S')

    current_port = TextField(index='CURRENT_PORT',
                             desc="The name of the Port the subject vessel is "
                                  "currently in (NULL if the vessel is underway)")

    current_port_id = NumberField(index='PORT_ID',
                                  desc="A uniquely assigned ID by "
                                       "MarineTraffic for the Current Port")

    current_port_unlocode = TextField(index='PORT_UNLOCODE',
                                      desc="A uniquely assigned ID by "
                                           "United Nations for the Current Port")

    last_port = TextField(index='LAST_PORT',
                          desc="The Name of the Last Port the vessel has visited")

    last_port_time = DatetimeField(index='LAST_PORT_TIME',
                                   desc="The Date and Time (in UTC) that the "
                                        "subject vessel departed from the Last Port",
                                   format='%Y-%m-%dT%H:%M:%S')

    last_port_id = NumberField(index='LAST_PORT_ID',
                               desc="A uniquely assigned ID by MarineTraffic for the Last Port")

    last_port_unlocode = TextField(index='LAST_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by "
                                        "United Nations for the Last Port")

    next_port_id = NumberField(index='NEXT_PORT_ID',
                               desc="A uniquely assigned ID by MarineTraffic for the Next Port")

    next_port_unlocode = TextField(index='NEXT_PORT_UNLOCODE',
                                   desc="A uniquely assigned ID by "
                                        "United Nations for the Next Port")

    next_port_name = TextField(index='NEXT_PORT_NAME',
                               desc="The Name of the Next Port as derived by MarineTraffic "
                                    "based on the subject vessel's reported Destination")

    next_port_country = TextField(index='NEXT_PORT_COUNTRY',
                                  desc="The Country that the Next Port is located at")

    eta_calc = DatetimeField(index='ETA_CALC',
                             desc="The Estimated Time of Arrival to Destination of "
                                  "the subject vessel according to the MarineTraffic calculations",
                             format='%Y-%m-%dT%H:%M:%S')
