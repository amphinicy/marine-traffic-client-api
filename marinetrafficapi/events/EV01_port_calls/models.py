from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, BooleanField, DatetimeField, TextField


class PortCall(Model):
    """Get all vessel historical positions for a specific period of time."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a \n"
                            "ine-digit number sent in digital form \n"
                            "over a radio frequency that identifies \n"
                            "the vessel's transmitter station")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    load_status = NumberField(index='LOAD_STATUS',
                              desc="The load status of the subject vessel \n"
                                   "(0 : N/A, 1 : In Ballast, \n"
                                   "2 : Partially Laden, 3 : Fully Laden)")

    voyage_avg_speed = NumberField(index='VOYAGE_SPEED_AVG',
                                   desc="Average Maintained Speed (in knots x10) \n"
                                        "since the last Port Call while steaming \n"
                                        "at speed > 5 knots - Updated upon Arriva")

    voyage_max_speed = NumberField(index='VOYAGE_SPEED_MAX',
                                   desc="Maximum Recorded Speed (in knots x10) \n"
                                        "since the last Port Call - \n"
                                        "Updated upon Arrival")

    local_timestamp = DatetimeField(index='TIMESTAMP_LT',
                                    desc="The Date and Time (in Local Time) \n"
                                         "of the Port Call",
                                    format='%Y-%m-%dT%H:%M:%S')

    utc_timestamp = DatetimeField(index='TIMESTAMP_UTC',
                                  desc="The Date and Time (in UTC) \n"
                                       "of the Port Call",
                                  format='%Y-%m-%dT%H:%M:%S')

    ship_id = NumberField(index='SHIP_ID',
                          desc="A uniquely assigned ID by \n"
                               "MarineTraffic for the subject vessel")

    move_type = BooleanField(index='MOVE_TYPE',
                             desc="0 or 1 - specifies the Port Call \n"
                                  "type (0 = Arrival, 1 = Departure)")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    port_id = NumberField(index='PORT_ID',
                          desc="A uniquely assigned ID by \n"
                               "MarineTraffic for the Current Port")

    port_name = TextField(index='PORT_NAME',
                          desc="The Type of the subject vessel")

    unlocode = TextField(index='UNLOCODE',
                         desc="A uniquely assigned ID by United \n"
                              "Nations for the subject Port")

    draught = NumberField(index='DRAUGHT',
                          desc="The Draught (in metres x10) of the \n"
                               "subject vessel according to the \n"
                               "AIS transmissions")

    port_operation = NumberField(index='PORT_OPERATION',
                                 desc="Indicates LOAD/DISCHARGE operations in \n"
                                      "the subject Port Call event \n"
                                      "(0 : N/A, 1 : load, 2 : discharge, \n"
                                      "3 : both, 4 : none)")

    in_transit = BooleanField(index='INTRANSIT',
                              desc="0 or 1 - specifies whether the vessel \n"
                                   "anchored in the Port or was In Transit \n"
                                   "(1 = In Transit)")

    distance_travelled = NumberField(index='DISTANCE_TRAVELLED',
                                     desc="The Distance (in NM) that the subject \n"
                                          "vessel has travelled since departing \n"
                                          "from Last Port")

    voyage_idle_time = NumberField(index='VOYAGE_IDLE_TIME_MINS',
                                   desc="Total time in minutes since the previous \n"
                                        "Port Call while the vessel stopped or \n"
                                        "moving at speed < 3 knots - \n"
                                        "Updated upon Arrival")

    elapsed_noanch = NumberField(index='ELAPSED_NOANCH',
                                 desc="Total time of Voyage since the \n"
                                      "previous Port Call except Anchorages \n"
                                      "and Canals - Updated upon Arrival")

    distance_leg = NumberField(index='DISTANCE_LEG',
                               desc="The distance (in NM) between the last \n"
                                    "two calls regardless of Port Type")

    comfleet_grouped_type = TextField(index='COMFLEET_GROUPEDTYPE',
                                      desc="The commercial market segment \n"
                                           "the subject vessel belongs to")

    ship_class = TextField(index='SHIPCLASS',
                           desc="The class of the subject vessel \n"
                                "based on vessel type and size")
