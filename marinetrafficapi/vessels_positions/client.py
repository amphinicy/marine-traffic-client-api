import click

from marinetrafficapi import constants
from marinetrafficapi.bind import bind_request

from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.models import VesselHistoricalPosition
from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.query_params import PS01QueryParams

from marinetrafficapi.vessels_positions.\
    PS02_PS06_vessel_positions.models import FleetVesselPosition
from marinetrafficapi.vessels_positions.\
    PS02_PS06_vessel_positions.query_params import PS02PS06QueryParams

from marinetrafficapi.vessels_positions.\
    PS07_single_vessel_positions.models import SingleVesselPosition
from marinetrafficapi.vessels_positions.\
    PS07_single_vessel_positions.query_params import PS07QueryParams


class VesselPositions:
    """Retrieve forecasted information for any vessel.
    Get ETA and voyage related information using one of these APIs."""

    vessel_historical_track = bind_request(
        api_path='/exportvesseltrack',
        model=VesselHistoricalPosition,
        query_parameters=PS01QueryParams,
        default_parameters={
            'v': '2',
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}: \nGet all historical positions \n'
                    'for one or more vessels over a period of time'
            .format(click.style("API CALL PS01", fg="red"))
    )

    fleet_vessel_positions = bind_request(
        api_path='/exportvessels',
        model=FleetVesselPosition,
        query_parameters=PS02PS06QueryParams,
        default_parameters={
            'v': '8',
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet positional information for a set of predefined vessels \n'
                    '{}:\nMonitor vessel activity for your MarineTraffic fleet(s)\n'
                    '{}:\nMonitor vessel activity in one or more ports of your interest\n'
                    '{}:\nMonitor vessel activity in an area of your interest\n'
                    '{}:\nRetrieve positions for vessels sailing in an area that \n'
                    'you define each time you call the service'
            .format(click.style("API CALL PS02", fg="red"),
                    click.style("API CALL PS03", fg="red"),
                    click.style("API CALL PS04", fg="red"),
                    click.style("API CALL PS05", fg="red"),
                    click.style("API CALL PS06", fg="red"))
    )

    single_vessel_positions = bind_request(
        api_path='/exportvessel',
        model=SingleVesselPosition,
        query_parameters=PS07QueryParams,
        default_parameters={
            'v': '5',
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet the latest available position or voyage \n'
                    'information for a particular vessel'
            .format(click.style("API CALL PS07", fg="red"))
    )
