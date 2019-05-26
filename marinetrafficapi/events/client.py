import click

from marinetrafficapi import constants
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

    port_calls = bind_request(
        api_path='/portcalls',
        model=PortCall,
        query_parameters=EV01QueryParams,
        default_parameters={
            'v': '4',
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet detailed arrival and departure \n'
                    'information for a port or vessel'
            .format(click.style("API CALL EV01", fg="red"))
    )

    vessel_events = bind_request(
        api_path='/vesselevents',
        model=VesselEvent,
        query_parameters=EV02QueryParams,
        default_parameters={
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nAccess our powerful events data \n'
                    'and event derived intelligence'
            .format(click.style("API CALL EV01", fg="red"))
    )

    berth_calls = bind_request(
        api_path='/berth-calls',
        model=BerthCall,
        query_parameters=EV03QueryParams,
        default_parameters={
            constants.ClientConst.MSG_TYPE: constants.ClientConst.SIMPLE,
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description='{}:\nGet berth arrival and departure information \n'
                    'for a specific vessel, berth, terminal or port'
            .format(click.style("API CALL EV01", fg="red"))
    )
