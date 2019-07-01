from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, TextField, RealNumberField


class PredictiveArrivals(Model):
    """Receive a prediction of the vessels
    likely to arrive to a specific port."""

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

    from_port_id = NumberField(index='FROM_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the port that \n"
                                    "was used as origin to retrieve \n"
                                    "possible destinations")

    from_port = TextField(index='FROM_PORT',
                          desc="The port that was used as origin \n"
                               "to retrieve possible destinations")

    next_port_id = NumberField(index='NEXT_PORT_ID',
                               desc="A uniquely assigned ID by \n"
                                    "MarineTraffic for the Next Port")

    next_port = TextField(index='NEXT_PORT',
                          desc="The target port used to \n"
                               "predict arrivals of vessels")

    next_area = TextField(index='NEXT_AREA',
                          desc="The area where the target port belongs to")

    next_port_prob = RealNumberField(index='NEXT_PORT_PROB',
                                     desc="The probability of visiting \n"
                                          "the target port")

    next_area_prob = RealNumberField(index='NEXT_AREA_PROB',
                                     desc="The probability of visiting the \n"
                                          "area where the target port is")
