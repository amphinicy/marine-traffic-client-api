class QueryParams:
    """Query parameters for API calls."""

    params = {}

    default_params = {
        # simple or extended (extended cost more credits)
        'msg_type': 'msgtype',

        # Response type. Use one of the following: xml, csv, json, jsono (object)
        'protocol': 'protocol'
    }

    def __init__(self):
        pass

    @classmethod
    def get_params(cls):
        return {**cls.params, **QueryParams.default_params}
