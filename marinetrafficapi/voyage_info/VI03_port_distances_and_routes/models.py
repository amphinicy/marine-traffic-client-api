from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, BooleanField, LinestringField


class PortDistanceAndRoute(Model):
    """Receive a list of available routes and distances
    from a specific point to a port or from port to port."""

    distance = NumberField(index='DISTANCE',
                           desc="The Distance (in NM) between the specified point "
                                "or port to the destination port")

    panama = BooleanField(index='PANAMA',
                          desc="Whether the vessel route passes via the Panama canal")

    suez = BooleanField(index='SUEZ',
                        desc="Whether the vessel route passes via the Suez canal")

    final_path = LinestringField(index='FINAL_PATH',
                                 desc="Route/Waypoints as Linestring "
                                      "Geometry in WKT - Well-Known Text")
