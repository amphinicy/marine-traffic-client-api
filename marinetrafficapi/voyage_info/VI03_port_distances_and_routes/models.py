from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, BooleanField, LinestringField


class PortDistanceAndRoute(Model):
    """Receive a list of available routes and distances
    from a specific point to a port or from port to port."""

    distance = NumberField(index='DISTANCE',
                           desc="The Distance (in NM) between \n"
                                "the specified point or port \n"
                                "to the destination port")

    panama = BooleanField(index='PANAMA',
                          desc="Whether the vessel route \n"
                               "passes via the Panama canal")

    suez = BooleanField(index='SUEZ',
                        desc="Whether the vessel route \n"
                             "passes via the Suez canal")

    final_path = LinestringField(index='FINAL_PATH',
                                 desc="Route/Waypoints as Linestring \n"
                                      "Geometry in WKT - Well-Known Text")
