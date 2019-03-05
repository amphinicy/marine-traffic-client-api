from marinetrafficapi.bind import bind_request

from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.models import VesselHistoricalPosition
from marinetrafficapi.vessels_positions.\
    PS02_PS06_vessel_positions.models import FleetVesselPosition

from marinetrafficapi.vessels_positions.\
    PS01_vessel_historical_track.query_params import PS01QueryParams
from marinetrafficapi.vessels_positions.\
    PS02_PS06_vessel_positions.query_params import PS02PS06QueryParams

from marinetrafficapi.vessels_positions.\
    PS07_single_vessel_positions.query_params import PS07QueryParams
from marinetrafficapi.vessels_positions.\
    PS07_single_vessel_positions.models import SingleVesselPosition


class VesselPositions:
    """Retrieve forecasted information for any vessel.
    Get ETA and voyage related information using one of these APIs."""

    # PS01 - Get all historical positions for one or more vessels over
    #        a period of time.
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
    # PS03 - Monitor vessel activity for your MarineTraffic fleet(s)
    # PS04 - Monitor vessel activity in one or more ports of your interest
    # PS05 - Monitor vessel activity in an area of your interest
    # PS06 - Retrieve positions for vessels sailing in an area that
    #        you define each time you call the service
    fleet_vessel_positions = bind_request(
        api_path='/exportvessels',
        model=FleetVesselPosition,
        query_parameters=PS02PS06QueryParams,
        default_parameters={
            'v': '8',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )

    # PS07 - Get the latest available position or voyage information for
    #        a particular vessel.
    single_vessel_positions = bind_request(
        api_path='/exportvessel',
        model=SingleVesselPosition,
        query_parameters=PS07QueryParams,
        default_parameters={
            'v': '5',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )
