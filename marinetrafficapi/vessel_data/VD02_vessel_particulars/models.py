from marinetrafficapi.models import Model
from marinetrafficapi.fields import TextField, NumberField, RealNumberField


class VesselParticural(Model):
    """Get vessel particulars (including type, dimensions, ownership etc)."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a nine-digit number \n"
                            "sent in digital form over a radio frequency that identifies \n"
                            "the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation number - a \n"
                           "seven-digit number that uniquely identifies vessels")

    name = TextField(index='NAME',
                     desc="The Name of the subject vessel")

    build_place = TextField(index='PLACE_OF_BUILD',
                            desc="The place the subject vessel was built at")

    build_year = NumberField(index='BUILD',
                             desc="The year that the subject vessel was built")

    breadth_extreme = RealNumberField(index='BREADTH_EXTREME',
                                      desc="The extreme breadth (in metres) of the subject vessel")

    summer_dwt = NumberField(index='SUMMER_DWT',
                             desc="Deadweight - a measure (in metric tons) \n"
                                  "of how much weight a vessel can safely carry \n"
                                  "(excluding the vessel's own weight)")

    displacement_summer = NumberField(index='DISPLACEMENT_SUMMER',
                                      desc="Displacement - a measure of the vessel's weight")

    call_sign = TextField(index='CALLSIGN',
                          desc="A uniquely designated identifier for \n"
                               "the vessel's transmitter station")

    flag = TextField(index='FLAG',
                     desc="The flag of the subject vessel according \n"
                          "to AIS transmissions")

    draught = RealNumberField(index='DRAUGHT',
                              desc="The Draught (in metres x10) of the subject vessel \n"
                                   "according to the AIS transmissions")

    overall_length = RealNumberField(index='LENGTH_OVERALL',
                                     desc="The Overall Length (in metres) of the subject vessel")

    fuel_consumption = TextField(index='FUEL_CONSUMPTION',
                                 desc="The Fuel Consumption of the subject vessel")

    max_speed = RealNumberField(index='SPEED_MAX',
                                desc="The Maximum Operational Speed of the subject vessel")

    condition_speed = RealNumberField(index='SPEED_SERVICE',
                                      desc="The Speed that the vessel is designed to sail \n"
                                           "under certain conditions")

    wet_cargo_capacity = NumberField(index='LIQUID_OIL',
                                     desc="The Capacity (in cubic metres) of the wet cargo \n"
                                          "the vessel can carry")

    owner = TextField(index='OWNER',
                      desc="The Owning Company of the subject vessel \n"
                           "(null if the Owner and the Manager are the same)")

    manager = TextField(index='MANAGER',
                        desc="The Managing Company of the subject vessel \n"
                             "(null if the Owner and the Manager are the same)")

    vessel_type = TextField(index='VESSEL_TYPE',
                            desc="The specific type of the subject vessel")

    manager_owner = TextField(index='MANAGER_OWNER',
                              desc="The Owning/Managing Company \n"
                                   "(null if the Owner is different than the Manager)")
