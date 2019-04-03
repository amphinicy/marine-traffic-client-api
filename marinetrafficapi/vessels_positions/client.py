import click

from marinetrafficapi.bind import bind_request
from marinetrafficapi.constants import (ClientConst, RequestConst,
                                        FormatterConst)

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
            ClientConst.MSG_TYPE: ClientConst.SIMPLE,
            RequestConst.PROTOCOL: FormatterConst.JSONO
        },
        description=f'{click.style("API CALL PS01", fg="red")}: \n'
                    'Get all historical positions \n'
                    'for one or more vessels over a period of time'
    )

    fleet_vessel_positions = bind_request(
        api_path='/exportvessels',
        model=FleetVesselPosition,
        query_parameters=PS02PS06QueryParams,
        default_parameters={
            'v': '8',
            ClientConst.MSG_TYPE: ClientConst.SIMPLE,
            RequestConst.PROTOCOL: FormatterConst.JSONO
        },
        description=f'{click.style("API CALL PS02", fg="red")}: \n'
                    'Get positional information for a set of predefined vessels \n'
                    f'{click.style("API CALL PS03", fg="red")}: \n'
                    'Monitor vessel activity for your MarineTraffic fleet(s)\n'
                    f'{click.style("API CALL PS04", fg="red")}: \n'
                    'Monitor vessel activity in one or more ports of your interest\n'
                    f'{click.style("API CALL PS05", fg="red")}: \n'
                    'Monitor vessel activity in an area of your interest\n'
                    f'{click.style("API CALL PS06", fg="red")}: \n'
                    'Retrieve positions for vessels sailing in an area that \n'
                    'you define each time you call the service'
    )

    single_vessel_positions = bind_request(
        api_path='/exportvessel',
        model=SingleVesselPosition,
        query_parameters=PS07QueryParams,
        default_parameters={
            'v': '5',
            ClientConst.MSG_TYPE: ClientConst.SIMPLE,
            RequestConst.PROTOCOL: FormatterConst.JSONO
        },
        description=f'{click.style("API CALL PS07", fg="red")}: \n'
                    'Get the latest available position or voyage \n'
                    'information for a particular vessel'
    )
