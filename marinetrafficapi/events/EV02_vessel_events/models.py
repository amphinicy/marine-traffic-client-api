from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, DatetimeField, TextField


class VesselEvent(Model):
    """Get event based intelligence for a vessel."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - a nine-digit number "
                            "sent in digital form over a radio frequency that identifies "
                            "the vessel's transmitter station")

    ship_name = TextField(index='SHIPNAME',
                          desc="The Ship name of the subject vessel")

    timestamp = DatetimeField(index='TIMESTAMP',
                              desc="The date and time (in UTC) that the subject "
                                   "Event was recorded by MarineTraffic",
                              format='%Y-%m-%dT%H:%M:%S')

    event_id = NumberField(index='EVENT_ID',
                           desc="The ID of the subject event - more")

    event_name = TextField(index='EVENT_NAME',
                           desc="The Name of the subject Event")

    event_content = TextField(index='EVENT_CONTENT',
                              desc="The description of the subject Event")
