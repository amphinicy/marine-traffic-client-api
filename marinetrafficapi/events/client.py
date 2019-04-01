from marinetrafficapi.bind import bind_request

from marinetrafficapi.events.\
    EV01_port_calls.models import PortCall
from marinetrafficapi.events.\
    EV01_port_calls.query_params import EV01QueryParams

from marinetrafficapi.events.\
    EV02_vessel_events.models import VesselEvent
from marinetrafficapi.events.\
    EV02_vessel_events.query_params import EV02QueryParams


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
