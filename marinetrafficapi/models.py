from copy import deepcopy
from typing import List, Any

from marinetrafficapi.fields import Field


class Model:
    """Abstract model class."""

    def __init__(self, item: Any):
        self.item = item

    @classmethod
    def process(cls, data: list) -> List[object]:
        """Transform raw data into models."""

        model_list = []

        # iterate over formatted data from API call
        for item in data:

            # instantiate model with one row of data
            model_object = cls(item)

            # iterate over model properties
            for model_property in cls.__dict__:

                # invoke model property
                property_object = getattr(model_object,
                                          model_property)

                # check if the model property
                # is an instance of Field class
                if isinstance(property_object, Field):

                    # convert raw property data into corespondent
                    # data type defined by the Field class
                    property_object.convert_item(model_object)

                    # set model property value with formatted data
                    setattr(model_object, model_property,
                            deepcopy(property_object))

            model_list.append(model_object)

        return model_list
