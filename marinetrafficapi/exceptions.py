class MarineTrafficException(Exception):
	"""Handle All Marine Traffic Exceptions"""


class MarineTrafficClientApiException(MarineTrafficException):
	"""Handle Client Exceptions"""


class MarineTrafficRequestApiException(MarineTrafficException):
	"""Handle Request Exceptions"""


class MarineTrafficFormatterException(MarineTrafficException):
	"""Handle Formatter Exceptions"""
