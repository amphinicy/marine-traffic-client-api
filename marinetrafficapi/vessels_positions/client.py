from marinetrafficapi.bind import bind_request

from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.models import VesselHistoricalPosition
from marinetrafficapi.vessels_positions.\
    PS02_vessel_positions_of_a_static_fleet.models import StaticFleetVesselPosition

from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.query_params import PS01QueryParams
from marinetrafficapi.vessels_positions.\
    PS02_vessel_positions_of_a_static_fleet.query_params import PS02QueryParams

from marinetrafficapi.vessels_positions.\
    PS03_vessel_position_of_a_dynamic_fleet.query_params import PS03QueryParams
from marinetrafficapi.vessels_positions.\
    PS03_vessel_position_of_a_dynamic_fleet.models import DynamicFleetVesselPosition


class VesselPositions:
    """Retrieve forecasted information for any vessel.
    Get ETA and voyage related information using one of these APIs."""

    # PS01 - Get all historical positions for one or more vessels over a period of time.
    vessel_historical_track = bind_request(
        api_path='/exportvesseltrack',
        model=VesselHistoricalPosition,
        query_parameters=PS01QueryParams,
        default_parameters={
            'v': '2',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )

    # PS02 - Get positional information for a set of predefined vessels.
    static_fleet_vessel_positions = bind_request(
        api_path='/exportvessels',
        model=StaticFleetVesselPosition,
        query_parameters=PS02QueryParams,
        default_parameters={
            'v': '8',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )

    # PS03 - Monitor vessel activity for your MarineTraffic fleet(s)
    dynamic_fleet_vessel_positions = bind_request(
        api_path='/exportvessels',
        model=DynamicFleetVesselPosition,
        query_parameters=PS03QueryParams,
        default_parameters={
            'v': '8',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )
