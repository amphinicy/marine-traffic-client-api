from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, RealNumberField


class PredictiveDestinations(Model):
    """Receive a prediction of the likely
    destination of a vessel or fleet of vessels."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a \n"
                            "nine-digit number sent in digital form \n"
                            "over a radio frequency that identifies \n"
                            "the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation number - a \n"
                           "seven-digit number that uniquely \n"
                           "identifies vessels")

    ship_id = NumberField(index='SHIP_ID',
                          desc="A uniquely assigned ID by MarineTraffic \n"
                               "for the subject vessel")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Shipname of the subject vessel")

    ship_class = TextField(index='SHIPCLASS',
                           desc="The class of the subject vessel \n"
                                "based on vessel type and size")

    market = TextField(index='MARKET',
                       desc="The commercial market segment \n"
                            "the subject vessel belongs to")

    manager = TextField(index='MANAGER',
                        desc="The Managing Company of the subject vessel \n"
                             "(null if the Owner and the Manager are the same)")

    owner = TextField(index='OWNER',
                      desc="The Owning Company of the subject vessel \n"
                           "(null if the Owner and the Manager are the same)")

    from_port_id = NumberField(index='FROM_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the port that \n"
                                    "was used as origin to retrieve \n"
                                    "possible destinations")

    from_port = TextField(index='FROM_PORT',
                          desc="The port that was used as origin \n"
                               "to retrieve possible destinations")

    next_port_1_id = NumberField(index='NEXT_PORT_1_ID',
                                 desc="A uniquely assigned ID by \n"
                                      "MarineTraffic for the most \n"
                                      "probable destination port from \n"
                                      "the given port of origin")

    next_port_1 = TextField(index='NEXT_PORT_1',
                            desc="Most probable destination port \n"
                                 "from the given port of origin")

    next_port_1_prob = RealNumberField(index='NEXT_PORT_1_PROB',
                                       desc="The probability of visiting the \n"
                                            "most likely destination port")

    next_area_1 = TextField(index='NEXT_AREA_1',
                            desc="The area where the most probable port is")

    next_area_1_prob = RealNumberField(index='NEXT_AREA_1_PROB',
                                       desc="The probability of visiting the \n"
                                            "area where the predicted port is")

    next_port_2_id = NumberField(index='NEXT_PORT_2_ID',
                                 desc="A uniquely assigned ID by \n"
                                      "MarineTraffic for the most \n"
                                      "probable destination port from \n"
                                      "the given port of origin")

    next_port_2 = TextField(index='NEXT_PORT_2',
                            desc="Most probable destination port \n"
                                 "from the given port of origin")

    next_port_2_prob = RealNumberField(index='NEXT_PORT_2_PROB',
                                       desc="The probability of visiting the \n"
                                            "most likely destination port")

    next_area_2 = TextField(index='NEXT_AREA_2',
                            desc="The area where the most probable port is")

    next_area_2_prob = RealNumberField(index='NEXT_AREA_2_PROB',
                                       desc="The probability of visiting the \n"
                                            "area where the predicted port is")

    next_port_3_id = NumberField(index='NEXT_PORT_3_ID',
                                 desc="A uniquely assigned ID by \n"
                                      "MarineTraffic for the most \n"
                                      "probable destination port from \n"
                                      "the given port of origin")

    next_port_3 = TextField(index='NEXT_PORT_3',
                            desc="Most probable destination port \n"
                                 "from the given port of origin")

    next_port_3_prob = RealNumberField(index='NEXT_PORT_3_PROB',
                                       desc="The probability of visiting the \n"
                                            "most likely destination port")

    next_area_3 = TextField(index='NEXT_AREA_3',
                            desc="The area where the most probable port is")

    next_area_3_prob = RealNumberField(index='NEXT_AREA_3_PROB',
                                       desc="The probability of visiting the \n"
                                            "area where the predicted port is")

    next_port_4_id = NumberField(index='NEXT_PORT_4_ID',
                                 desc="A uniquely assigned ID by \n"
                                      "MarineTraffic for the most \n"
                                      "probable destination port from \n"
                                      "the given port of origin")

    next_port_4 = TextField(index='NEXT_PORT_4',
                            desc="Most probable destination port \n"
                                 "from the given port of origin")

    next_port_4_prob = RealNumberField(index='NEXT_PORT_4_PROB',
                                       desc="The probability of visiting the \n"
                                            "most likely destination port")

    next_area_4 = TextField(index='NEXT_AREA_4',
                            desc="The area where the most probable port is")

    next_area_4_prob = RealNumberField(index='NEXT_AREA_4_PROB',
                                       desc="The probability of visiting the \n"
                                            "area where the predicted port is")

    next_port_5_id = NumberField(index='NEXT_PORT_5_ID',
                                 desc="A uniquely assigned ID by \n"
                                      "MarineTraffic for the most \n"
                                      "probable destination port from \n"
                                      "the given port of origin")

    next_port_5 = TextField(index='NEXT_PORT_5',
                            desc="Most probable destination port \n"
                                 "from the given port of origin")

    next_port_5_prob = RealNumberField(index='NEXT_PORT_5_PROB',
                                       desc="The probability of visiting the \n"
                                            "most likely destination port")

    next_area_5 = TextField(index='NEXT_AREA_5',
                            desc="The area where the most probable port is")

    next_area_5_prob = RealNumberField(index='NEXT_AREA_5_PROB',
                                       desc="The probability of visiting the \n"
                                            "area where the predicted port is")
