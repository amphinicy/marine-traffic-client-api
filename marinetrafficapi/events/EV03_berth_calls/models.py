from marinetrafficapi.models import Model
from marinetrafficapi.fields import (NumberField, RealNumberField,
                                     DatetimeField, TextField)


class BerthCall(Model):
    """Get berth arrival and departure information for a
    specific vessel, berth, terminal or port."""

    ship_id = NumberField(index='SHIP_ID',
                          desc="Api Rspfield Shipid.")

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - \n"
                            "a nine-digit number sent in digital \n"
                            "form over a radio frequency that \n"
                            "identifies the vessel's transmitter station")

    imo = NumberField(index='IMO',
                      desc="International Maritime Organisation number - \n"
                           "a seven-digit number that uniquely \n"
                           "identifies vessels")

    dock_local_time = DatetimeField(index='DOCK_TIMESTAMP_LT',
                                    desc="The Date and Time (in Local Time) \n"
                                         "the subject vessel was Docked at the Berth",
                                    format='%Y-%m-%d %H:%M:%S')

    dock_utc_time = DatetimeField(index='DOCK_TIMESTAMP_UTC',
                                  desc="The Date and Time (in UTC) the subject \n"
                                       "vessel was Docked at the Berth",
                                  format='%Y-%m-%d %H:%M:%S')

    dock_offset_time = RealNumberField(index='DOCK_TIMESTAMP_OFFSET',
                                       desc="The time zone offset at the \n"
                                            "time of arrival/docking")

    undock_local_time = DatetimeField(index='UNDOCK_TIMESTAMP_LT',
                                      desc="The Date and Time (in Local Time) \n"
                                           "the subject vessel was Undocked \n"
                                           "from the Berth",
                                      format='%Y-%m-%d %H:%M:%S')

    undock_utc_time = DatetimeField(index='UNDOCK_TIMESTAMP_UTC',
                                    desc="The Date and Time (in UTC) the \n"
                                         "subject vessel was Undocked \n"
                                         "from the Berth",
                                    format='%Y-%m-%d %H:%M:%S')

    undock_offset_time = RealNumberField(index='UNDOCK_TIMESTAMP_OFFSET',
                                         desc="The time zone offset at the \n"
                                              "time of undocking/departure")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    type_name = TextField(index='TYPE_NAME',
                          desc="The Type of the subject vessel")

    grt = NumberField(index='GRT',
                      desc="Gross Tonnage - unitless measure that \n"
                           "calculates the moulded volume of all \n"
                           "enclosed spaces of a ship")

    dwt = NumberField(index='DWT',
                      desc="Deadweight - a measure (in metric tons) \n"
                           "of how much weight a vessel can safely \n"
                           "carry (excluding the vessel's own weight")

    flag = TextField(index='FLAG',
                     desc="The flag of the subject vessel \n"
                          "according to AIS transmissions")

    year_built = NumberField(index='YEAR_BUILT',
                             desc="The year that the subject vessel was built")

    berth_id = NumberField(index='BERTH_ID',
                           desc="A uniquely assigned ID by \n"
                                "MarineTraffic for the Current Berth")

    berth_name = TextField(index='BERTH_NAME',
                           desc="The Name of the subject Berth")

    terminal_id = NumberField(index='TERMINAL_ID',
                              desc="A uniquely assigned ID by MarineTraffic \n"
                                   "for the Terminal where the Berth belongs \n"
                                   "(if available)")

    terminal_name = TextField(index='TERMINAL_NAME',
                              desc="The Name of the Terminal where \n"
                                   "the Berth belongs (if available)")

    port_name = TextField(index='PORT_NAME',
                          desc="The Name of the subject Port")

    port_id = NumberField(index='PORT_ID',
                          desc="A uniquely assigned ID by \n"
                               "MarineTraffic for the Current Port")

    unlocode = TextField(index='UNLOCODE',
                         desc="A uniquely assigned ID by \n"
                              "United Nations for the subject Port")

    country_code = TextField(index='COUNTRY_CODE',
                             desc="The Country of the subject Port")

    destination_id = NumberField(index='DESTINATION_ID',
                                 desc="Api Rspfield Destination Id")

    destination = TextField(index='DESTINATION',
                            desc="The Destination of the subject \n"
                                 "vessel according to the AIS transmissions")

    arrival_local_time = DatetimeField(index='ARR_TIMESTAMP_LT',
                                       desc="The Date and Time (in Local Time) the \n"
                                            "subject vessel arrived at the port, \n"
                                            "before the docking",
                                       format='%Y-%m-%d %H:%M:%S')

    arrival_utc_time = DatetimeField(index='ARR_TIMESTAMP_UTC',
                                     desc="The Date and Time (in UTC) the subject \n"
                                          "vessel arrived at the port, before \n"
                                          "the docking",
                                     format='%Y-%m-%d %H:%M:%S')

    arrival_draught = NumberField(index='ARR_DRAUGHT',
                                  desc="The Draught (in metres x10) of the subject \n"
                                       "vessel, at the time of arrival, \n"
                                       "according to the AIS transmissions")

    arrival_load_status = NumberField(index='ARR_LOAD_STATUS',
                                      desc="The load status of the subject vessel \n"
                                           "(0 : N/A, 1 : In Ballast, 2 : Partially Laden, \n"
                                           "3 : Fully Laden) at the time of arrival")

    distance_travelled = NumberField(index='DISTANCE_TRAVELLED',
                                     desc="The Distance (in NM) that the subject \n"
                                          "vessel has travelled since departing \n"
                                          "from Last Port")

    voyage_average_speed = NumberField(index='VOYAGE_SPEED_AVG',
                                       desc="Average Maintained Speed (in knots x10) \n"
                                            "since the last Port Call while steaming \n"
                                            "at speed > 5 knots - Updated upon Arrival")

    voyage_max_speed = NumberField(index='VOYAGE_SPEED_MAX',
                                   desc="Maximum Recorded Speed (in knots x10) \n"
                                        "since the last Port Call - \n"
                                        "Updated upon Arrival")

    voyage_idle_time = NumberField(index='VOYAGE_IDLE_TIME_MINS',
                                   desc="Total time in minutes since the previous \n"
                                        "Port Call while the vessel stopped or \n"
                                        "moving at speed < 3 knots - \n"
                                        "Updated upon Arrival")

    origin_name = TextField(index='PREVIOUS_NOANCH_NAME',
                            desc="The name of the port of origin")

    origin_port_id = NumberField(index='PREVIOUS_NOANCH_ID',
                                 desc="The ID of the port of origin")

    origin_departure_time = DatetimeField(index='PREVIOUS_NOANCH_TIMESTAMP',
                                          desc="The time of Departure form the \n"
                                               "port of origin (UTC)",
                                          format='%Y-%m-%d %H:%M:%S')

    total_voyage_time = NumberField(index='ELAPSED_NOANCH',
                                    desc="Total time of Voyage since the previous \n"
                                         "Port Call except Anchorages and Canals - \n"
                                         "Updated upon Arrival")

    departure_local_time = DatetimeField(index='DEP_TIMESTAMP_LT',
                                         desc="The Date and Time (in Local Time) \n"
                                              "the subject vessel departed from the \n"
                                              "port, after the undocking",
                                         format='%Y-%m-%d %H:%M:%S')

    departure_utc_time = DatetimeField(index='DEP_TIMESTAMP_UTC',
                                       desc="The Date and Time (in UTC) the subject \n"
                                            "vessel departed from the port, \n"
                                            "after the undocking",
                                       format='%Y-%m-%d %H:%M:%S')

    departure_draught = NumberField(index='DEP_DRAUGHT',
                                    desc="The Draught (in metres x10) of the \n"
                                         "subject vessel, at the time of departure, \n"
                                         "according to the AIS transmission")

    departure_load_status = NumberField(index='DEP_LOAD_STATUS',
                                        desc="The load status of the subject vessel \n"
                                             "(0 : N/A, 1 : In Ballast, 2 : Partially Laden, \n"
                                             "3 : Fully Laden) at the time of departure")

    port_operation = NumberField(index='PORT_OPERATION',
                                 desc="Indicates LOAD/DISCHARGE operations in \n"
                                      "the subject Port Call event (0 : N/A, \n"
                                      "1 : load, 2 : discharge, 3 : both, 4 : none)")

    time_at_berth = NumberField(index='TIME_AT_BERTH',
                                desc="The total time in minutes that \n"
                                     "the vessel stayed at berth")

    time_at_port = NumberField(index='TIME_AT_PORT',
                               desc="The total time in minutes that \n"
                                    "the vessel stayed at port")
