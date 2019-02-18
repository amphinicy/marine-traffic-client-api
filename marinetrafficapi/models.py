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

        for item in data:
            model_object = cls(item)

            for model_property in cls.__dict__:
                property_object = getattr(model_object,
                                          model_property)

                if isinstance(property_object, Field):
                    property_object.convert_item(model_object)
                    setattr(model_object, model_property,
                            property_object.data)

            model_list.append(model_object)

        return model_list
