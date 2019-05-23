import click

from marinetrafficapi import constants
from marinetrafficapi.bind import bind_request

from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.models import PortDistanceAndRoute
from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.query_params import VI03QueryParams

from marinetrafficapi.voyage_info.\
    VI01_voyage_forecasts.models import VoyageForecast
from marinetrafficapi.voyage_info.\
    VI01_voyage_forecasts.query_params import VI01QueryParams


class VoyageInfo:
    """Retrieve forecasted information for any vessel.
    Get ETA and voyage related information using one of these APIs."""

    voyage_forecasts = bind_request(
        api_path='/voyageforecast',
        model=VoyageForecast,
        query_parameters=VI01QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description=f'{click.style("API CALL VI01", fg="red")}: \n'
                    'Get a voyage forecast for a vessel or \n'
                    'your MarineTraffic fleet'
    )

    port_distances_and_routes = bind_request(
        api_path='/exportroutes',
        model=PortDistanceAndRoute,
        query_parameters=VI03QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description=f'{click.style("API CALL VI03", fg="red")}: \n'
                    'Get all the available vessel routes and the respective \n'
                    'distances from point to port or port to port'
    )
