from marinetrafficapi.models import Model
from marinetrafficapi.fields import TextField, NumberField


class SearchVessel(Model):
    """Search MarineTraffic database for a vessel."""

    id = NumberField(index='SHIP_ID',
                     desc="A uniquely assigned ID by MarineTraffic \n"
                          "for the subject vessel")

    name = TextField(index='SHIPNAME',
                     desc="The Shipname of the subject vessel")

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - \n"
                            "a nine-digit number sent in digital \n"
                            "form over a radio frequency that \n"
                            "identifies the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation \n"
                           "number - a seven-digit number that \n"
                           "uniquely identifies vessels")

    build_year = NumberField(index='YEAR_BUILT',
                             desc="The year that the subject vessel was built")

    dwt = NumberField(index='DWT',
                      desc="Deadweight - a measure (in metric tons) \n"
                           "of how much weight a vessel can safely carry \n"
                           "(excluding the vessel's own weight)")

    call_sign = TextField(index='CALLSIGN',
                          desc="A uniquely designated identifier for \n"
                               "the vessel's transmitter station")

    flag = TextField(index='FLAG',
                     desc="The flag of the subject vessel according \n"
                          "to AIS transmissions")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    details_page_url = TextField(index='MT_URL',
                                 desc="URL to the Details page of the \n"
                                      "subject vessel at MarineTraffic")

    country = TextField(index='COUNTRY',
                        desc="The country of the subject vessel \n"
                             "according to AIS transmissions")
