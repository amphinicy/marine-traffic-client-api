from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, BooleanField, DatetimeField, TextField


class PortCall(Model):
    """Get all vessel historical positions for a specific period of time."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a nine-digit number "
                            "sent in digital form over a radio frequency that identifies "
                            "the vessel's transmitter station")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    load_status = NumberField(index='LOAD_STATUS',
                              desc="The load status of the subject vessel "
                                   "(0 : N/A, 1 : In Ballast, 2 : Partially Laden, "
                                   "3 : Fully Laden)")

    voyage_avg_speed = NumberField(index='VOYAGE_SPEED_AVG',
                                   desc="Average Maintained Speed (in knots x10) since "
                                        "the last Port Call while steaming at speed > 5 "
                                        "knots - Updated upon Arriva")

    voyage_max_speed = NumberField(index='VOYAGE_SPEED_MAX',
                                   desc="Maximum Recorded Speed (in knots x10) since "
                                        "the last Port Call - Updated upon Arrival")

    local_timestamp = DatetimeField(index='TIMESTAMP_LT',
                                    desc="The Date and Time (in Local Time) of the Port Call",
                                    format='%Y-%m-%dT%H:%M:%S')

    utc_timestamp = DatetimeField(index='TIMESTAMP_UTC',
                                  desc="The Date and Time (in UTC) of the Port Call",
                                  format='%Y-%m-%dT%H:%M:%S')

    ship_id = NumberField(index='SHIP_ID',
                          desc="A uniquely assigned ID by MarineTraffic "
                               "for the subject vessel")

    move_type = BooleanField(index='MOVE_TYPE',
                             desc="0 or 1 - specifies the Port Call type "
                                  "(0 = Arrival, 1 = Departure)")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    port_id = NumberField(index='PORT_ID',
                          desc="A uniquely assigned ID by MarineTraffic for the Current Port")

    port_name = TextField(index='PORT_NAME',
                          desc="The Type of the subject vessel")

    unlocode = TextField(index='UNLOCODE',
                         desc="A uniquely assigned ID by United Nations for the subject Port")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the subject vessel "
                               "according to the AIS transmissions")

    port_operation = NumberField(index='PORT_OPERATION',
                                 desc="Indicates LOAD/DISCHARGE operations in the subject "
                                      "Port Call event (0 : N/A, 1 : load, 2 : discharge, "
                                      "3 : both, 4 : none)")

    in_transit = BooleanField(index='INTRANSIT',
                              desc="0 or 1 - specifies whether the vessel anchored in the "
                                   "Port or was In Transit (1 = In Transit)")

    distance_travelled = NumberField(index='DISTANCE_TRAVELLED',
                                     desc="The Distance (in NM) that the subject vessel "
                                          "has travelled since departing from Last Port")

    voyage_idle_time = NumberField(index='VOYAGE_IDLE_TIME_MINS',
                                   desc="Total time in minutes since the previous Port Call "
                                        "while the vessel stopped or moving at speed < 3 "
                                        "knots - Updated upon Arrival")

    elapsed_noanch = NumberField(index='ELAPSED_NOANCH',
                                 desc="Total time of Voyage since the previous Port Call "
                                      "except Anchorages and Canals - Updated upon Arrival")

    distance_leg = NumberField(index='DISTANCE_LEG',
                               desc="The distance (in NM) between the last two calls "
                                    "regardless of Port Type")

    comfleet_grouped_type = TextField(index='COMFLEET_GROUPEDTYPE',
                                      desc="The commercial market segment the "
                                           "subject vessel belongs to")

    ship_class = TextField(index='SHIPCLASS',
                           desc="The class of the subject vessel based on vessel type and size")
