import click

from marinetrafficapi import constants
from marinetrafficapi.bind import bind_request

from marinetrafficapi.voyage_info.\
    VI01_voyage_forecasts.models import VoyageForecast
from marinetrafficapi.voyage_info.\
    VI01_voyage_forecasts.query_params import VI01QueryParams

from marinetrafficapi.voyage_info.\
    VI02_expected_arrivals.models import ExpectedArrival
from marinetrafficapi.voyage_info.\
    VI02_expected_arrivals.query_params import VI02QueryParams

from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.models import PortDistanceAndRoute
from marinetrafficapi.voyage_info.\
    VI03_port_distances_and_routes.query_params import VI03QueryParams

from marinetrafficapi.voyage_info.\
    VI04_predictive_destinations.models import PredictiveDestinations
from marinetrafficapi.voyage_info.\
    VI04_predictive_destinations.query_params import VI04QueryParams

from marinetrafficapi.voyage_info.\
    VI05_predictive_arrivals.models import PredictiveArrivals
from marinetrafficapi.voyage_info.\
    VI05_predictive_arrivals.query_params import VI05QueryParams

from marinetrafficapi.voyage_info.\
    VI06_port_congestion.models import PortCongestion
from marinetrafficapi.voyage_info.\
    VI06_port_congestion.query_params import VI06QueryParams

from marinetrafficapi.voyage_info.\
    VI07_eta_to_port.models import EtaToPort
from marinetrafficapi.voyage_info.\
    VI07_eta_to_port.query_params import VI07QueryParams


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
        description='{}:\nGet a voyage forecast for a vessel or \n'
                    'your MarineTraffic fleet'
            .format(click.style("API CALL VI01", fg="red"))
    )

    expected_arrivals = bind_request(
        api_path='/expectedarrivals',
        model=ExpectedArrival,
        query_parameters=VI02QueryParams,
        default_parameters={
            'v': '3',
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet expected arrivals to a specific port or country'
            .format(click.style("API CALL VI02", fg="red"))
    )

    port_distances_and_routes = bind_request(
        api_path='/exportroutes',
        model=PortDistanceAndRoute,
        query_parameters=VI03QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet all the available vessel routes and the \n'
                    'respective distances from point to port or port to port'
            .format(click.style("API CALL VI03", fg="red"))
    )

    predictive_destinations = bind_request(
        api_path='/predictive-destination-areas',
        model=PredictiveDestinations,
        query_parameters=VI04QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nReceive a prediction of the likely \n'
                    'destination of a vessel or fleet of vessels'
            .format(click.style("API CALL VI04", fg="red"))
    )

    predictive_arrivals = bind_request(
        api_path='/predictive-arrivals',
        model=PredictiveArrivals,
        query_parameters=VI05QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nReceive a prediction of the vessels \n'
                    'likely to arrive to a specific port'
            .format(click.style("API CALL VI05", fg="red"))
    )

    port_congestion = bind_request(
        api_path='/port-congestion',
        model=PortCongestion,
        query_parameters=VI06QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nReceive the Port Congestion \n'
                    'for a specific period of time'
            .format(click.style("API CALL VI06", fg="red"))
    )

    eta_to_port = bind_request(
        api_path='/etatoport',
        model=EtaToPort,
        query_parameters=VI07QueryParams,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet ETA and voyage information for a \n'
                    'vessel of your choice, to any port you define'
            .format(click.style("API CALL VI07", fg="red"))
    )
