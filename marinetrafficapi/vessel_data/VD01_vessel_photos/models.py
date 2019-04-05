from marinetrafficapi.models import Model
from marinetrafficapi.fields import TextField


class VesselPhoto(Model):
    """Retrieve the most popular photo of a vessel."""

    url = TextField(index='URL', desc="The URL of the photo")
