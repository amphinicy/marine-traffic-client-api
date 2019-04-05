import click

from marinetrafficapi.bind import bind_request
from marinetrafficapi.constants import (ClientConst, RequestConst,
                                        FormatterConst)

from marinetrafficapi.vessel_data.\
    VD01_vessel_photos.models import VesselPhoto
from marinetrafficapi.vessel_data.\
    VD01_vessel_photos.query_params import VD01QueryParams


class VesselData:
    """Retrieve details or photos of any vessel.
    Get general or technical information about
    any vessel using one of these APIs."""

    vessel_photos = bind_request(
        api_path='/exportvesselphoto',
        model=VesselPhoto,
        query_parameters=VD01QueryParams,
        default_parameters={
            ClientConst.MSG_TYPE: ClientConst.SIMPLE,
            RequestConst.PROTOCOL: FormatterConst.XML
        },
        description=f'{click.style("API CALL VD01", fg="red")}: \n'
                    'Get the most popular photo for a vessel \n'
                    'from the MarineTraffic photo database'
    )
