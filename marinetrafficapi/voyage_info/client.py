from marinetrafficapi.bind import bind_request

from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.models import PortDistanceAndRoute

from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.query_params import VI03QueryParams


class VoyageInfo:
    """Retrieve forecasted information for any vessel.
    Get ETA and voyage related information using one of these APIs."""

    # VI03 - Get all the available vessel routes and the respective
    # distances from point to port or port to port.
    port_distances_and_routes = bind_request(
        api_path='/exportroutes',
        model=PortDistanceAndRoute,
        query_parameters=VI03QueryParams,
        default_parameters={
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )
