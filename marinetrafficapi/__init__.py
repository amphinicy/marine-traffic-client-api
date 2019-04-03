# Main API class
from marinetrafficapi.client import Client as MarineTrafficApi

# Category API subclasses
from marinetrafficapi.events.client import Events
from marinetrafficapi.voyage_info.client import VoyageInfo
from marinetrafficapi.vessels_positions.client import VesselPositions

# Exception classes
from marinetrafficapi.exceptions import (MarineTrafficRequestApiException,
                                         MarineTrafficClientApiException,
                                         MarineTrafficFormatterException)
