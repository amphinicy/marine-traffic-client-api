from marinetrafficapi.voyage_info.client import VoyageInfo
from marinetrafficapi.vessels_positions.client import VesselPositions
from marinetrafficapi.exceptions import MarineTrafficRequestApiException


class Client(VesselPositions, VoyageInfo):
    """Main API class. Sets all API calls."""

    base_url = 'services.marinetraffic.com/en'
    base_path = '/api'
    protocol = 'https'

    def __init__(self, api_key: str = None, debug: bool = False,
                 fake_response_path: str = None):
        if not api_key:
            raise MarineTrafficRequestApiException('API key missing!')

        self.api_key = api_key
        self.debug = debug
        self.fake_response_path = fake_response_path
