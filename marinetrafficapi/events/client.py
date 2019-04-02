from marinetrafficapi.bind import bind_request

from marinetrafficapi.events.\
    EV01_port_calls.models import PortCall
from marinetrafficapi.events.\
    EV01_port_calls.query_params import EV01QueryParams

from marinetrafficapi.events.\
    EV02_vessel_events.models import VesselEvent
from marinetrafficapi.events.\
    EV02_vessel_events.query_params import EV02QueryParams

from marinetrafficapi.events.\
    EV03_berth_calls.models import BerthCall
from marinetrafficapi.events.\
    EV03_berth_calls.query_params import EV03QueryParams


class Events:
    """Retrieve event information of any vessel.
    Select which events, including port calls and
    departures, using any of these APIs."""

    # EV01 - Get detailed arrival and departure
    #        information for a port or vessel.
    port_calls = bind_request(
        api_path='/portcalls',
        model=PortCall,
        query_parameters=EV01QueryParams,
        default_parameters={
            'v': '4',
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )

    # EV02 - Access our powerful events data
    #        and event derived intelligence.
    vessel_events = bind_request(
        api_path='/vesselevents',
        model=VesselEvent,
        query_parameters=EV02QueryParams,
        default_parameters={
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )

    # EV03 - Get berth arrival and departure information
    #        for a specific vessel, berth, terminal or port.
    berth_calls = bind_request(
        api_path='/berth-calls',
        model=BerthCall,
        query_parameters=EV03QueryParams,
        default_parameters={
            'msgtype': 'simple',
            'protocol': 'jsono'
        }
    )
