import click

from marinetrafficapi.events.client import Events
from marinetrafficapi.voyage_info.client import VoyageInfo
from marinetrafficapi.vessel_data.client import VesselData
from marinetrafficapi.vessels_positions.client import VesselPositions
from marinetrafficapi.exceptions import MarineTrafficRequestApiException


class Client(VesselPositions, VoyageInfo, Events, VesselData):
    """Main API class. Sets all API calls."""

    base_url = 'services.marinetraffic.com'
    base_path = '/api'
    protocol = 'https'

    def __init__(self, api_key: str = None, debug: bool = False,
                 fake_response_path: str = None):
        if not api_key:
            raise MarineTrafficRequestApiException('API key missing!')

        self.request = None
        self.api_key = api_key
        self.debug = debug
        self.fake_response_path = fake_response_path

    @classmethod
    def print_params_for(cls, fn_name: str) -> None:
        """Prints parameters for certain API call function."""

        try:
            getattr(cls, fn_name)(None, print_params=True)
        except AttributeError:
            click.secho(f'Unknown API method: {fn_name}', fg='red')
