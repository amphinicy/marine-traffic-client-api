from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, DatetimeField, TextField


class VesselEvent(Model):
    """Get event based intelligence for a vessel."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - \n"
                            "a nine-digit number sent in digital \n"
                            "form over a radio frequency that \n"
                            "identifies the vessel's transmitter station")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    timestamp = DatetimeField(index='TIMESTAMP',
                              desc="The date and time (in UTC) that \n"
                                   "the subject Event was recorded by \n"
                                   "MarineTraffic",
                              format='%Y-%m-%dT%H:%M:%S')

    event_id = NumberField(index='EVENT_ID',
                           desc="The ID of the subject event - more")

    event_name = TextField(index='EVENT_NAME',
                           desc="The Name of the subject Event")

    event_content = TextField(index='EVENT_CONTENT',
                              desc="The description of the subject Event")
