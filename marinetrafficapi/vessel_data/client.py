import click

from marinetrafficapi import constants
from marinetrafficapi.formatter import Xml
from marinetrafficapi.bind import bind_request

from marinetrafficapi.vessel_data.\
    VD01_vessel_photos.models import VesselPhoto
from marinetrafficapi.vessel_data.\
    VD01_vessel_photos.query_params import VD01QueryParams

from marinetrafficapi.vessel_data.\
    VD02_vessel_particulars.models import VesselParticural
from marinetrafficapi.vessel_data.\
    VD02_vessel_particulars.query_params import VD02QueryParams

from marinetrafficapi.vessel_data.\
    VD03_search_vessel.models import SearchVessel
from marinetrafficapi.vessel_data.\
    VD03_search_vessel.query_params import VD03SearchVessel


class VesselData:
    """Retrieve details or photos of any vessel.
    Get general or technical information about
    any vessel using one of these APIs."""

    vessel_photos = bind_request(
        api_path='/exportvesselphoto',
        model=VesselPhoto,
        formatter=Xml,
        query_parameters=VD01QueryParams,
        description=f'{click.style("API CALL VD01", fg="red")}: \n'
                    'Get the most popular photo for a vessel \n'
                    'from the MarineTraffic photo database'
    )

    vessel_particulars = bind_request(
        api_path='/vesselmasterdata',
        model=VesselParticural,
        query_parameters=VD02QueryParams,
        default_parameters={
            'v': '3',
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description=f'{click.style("API CALL VD02", fg="red")}: \n'
                    'Get vessel particulars (including \n'
                    'type, dimensions, ownership etc).'
    )

    search_vessel = bind_request(
        api_path='/shipsearch',
        model=SearchVessel,
        query_parameters=VD03SearchVessel,
        default_parameters={
            constants.RequestConst.PROTOCOL: constants.FormatterConst.JSONO
        },
        description=f'{click.style("API CALL VD03", fg="red")}: \n'
                    'Search MarineTraffic database for a vessel.'
    )
