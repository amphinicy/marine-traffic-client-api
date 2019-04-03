import requests
from typing import TYPE_CHECKING, Union

from marinetrafficapi.debug import Debug
from marinetrafficapi.reponse import Response
from marinetrafficapi.formatter import FormatterFactory
from marinetrafficapi.exceptions import MarineTrafficRequestApiException
from marinetrafficapi.constants import (RequestConst, ResponseConst,
                                        ClientConst, TestConst,
                                        ResponseCode, BoolConst)

if TYPE_CHECKING:
    from marinetrafficapi.client import Client


def bind_request(**request_data) -> 'callable':
    """Binds request class to client property, dynamically."""

    class ApiRequest(object):
        """Request class. Does the actual API request."""

        model = request_data.get(ClientConst.MODEL)
        api_path = request_data.get(RequestConst.API_PATH)
        method = request_data.get(RequestConst.METHOD, RequestConst.GET)
        query_parameters = request_data.get(RequestConst.QUERY_PARAMETERS)
        default_parameters = request_data.get(RequestConst.DEFAULT_PARAMETERS)
        fake_response_path = request_data.get(TestConst.FAKE_RESPONSE_PATH)

        def __init__(self, client: 'Client', debug: 'Debug',
                     *path_params, **query_params):
            client.request = self

            self.url = None
            self.debug = debug
            self.client = client
            self.parameters = {RequestConst.QUERY: {},
                               RequestConst.PATH: []}

            self._timeout = 5

            self._set_parameters(*path_params, **query_params)

        def _set_parameters(self, *path_params, **query_params) -> None:
            """
            Prepares the list of query parameters
            :path_params: list of path parameters
            :query_params: dict of query parameters
            :return: None
            """

            # take timeout
            try:
                self._timeout = int(query_params.get(RequestConst.TIMEOUT,
                                                     self._timeout))
            except ValueError:
                pass
            try:
                del query_params[RequestConst.TIMEOUT]
            except KeyError:
                pass

            # set default API call params
            for key, value in self.default_parameters.items():
                self.parameters[RequestConst.QUERY][key] = value

            _query_params = self.query_parameters.get_params()

            # set API call params defined during the "call" invocation
            for key, value in query_params.items():
                if value is None:
                    continue

                if key in _query_params.values():
                    self.parameters[RequestConst.QUERY][key] = value

                elif key in _query_params.keys():
                    self.parameters[RequestConst.QUERY][_query_params[key]] = value

            # transform all True and False param to 1 and 0
            for key, value in self.parameters[RequestConst.QUERY].items():
                if value is True:
                    self.parameters[RequestConst.QUERY][key] = BoolConst.TRUE
                if value is False:
                    self.parameters[RequestConst.QUERY][key] = BoolConst.FALSE

            # set optional url path params
            for value in path_params:
                self.parameters[RequestConst.PATH].append(value)

        def _prepare_url(self) -> str:
            """
            Prepares url and query parameters for the request
            :return: URL
            """

            base_url = f'{self.client.protocol}://{self.client.base_url}' \
                       f'{self.client.base_path}{self.api_path}/{self.client.api_key}'

            url_parts = '/'.join([part for part in
                                  self.parameters[RequestConst.PATH]])

            url_query = '/'.join([f'{key}:{value}'
                                  for key, value in self.parameters[
                                      RequestConst.QUERY].items()])

            if url_parts:
                final_url = f'{base_url}/{url_parts}/{url_query}'
            else:
                final_url = f'{base_url}/{url_query}'

            self.debug.ok('url', f'{base_url}{url_parts}')
            self.debug.ok(RequestConst.QUERY_PARAMETERS,
                          self.parameters[RequestConst.QUERY])
            self.debug.ok('final url', final_url)

            return final_url

        def _do_request(self, url: str) -> (int, dict):
            """
            Makes the request to Marine Traffic Api servers
            :url: Url for the request
            :return: Tuple with two elements, status code and content
            """

            if self.client.fake_response_path:
                with open(self.client.fake_response_path, 'r') as f:
                    return ResponseCode.OK, f.read()

            elif self.method == RequestConst.GET:
                response = requests.get(url, timeout=self._timeout)
                self.debug.ok(ResponseConst.RESPONSE_OBJECT, response)
                return response.status_code, response.text

            else:
                # For future POST, PUT, DELETE requests
                return ResponseCode.NOT_FOUND, {}

        def _process_response(self, status_code: int, response: str) -> 'Response':
            """
            Process response using models
            :status_code: Response status code
            :response: Content
            :return: Response object
            """

            formatter = FormatterFactory(
                self.parameters[RequestConst.QUERY][RequestConst.PROTOCOL])\
                .get_formatter()

            response = Response(response, status_code, formatter, self)

            error_response = response.to_list
            if 'errors' in error_response:
                # error responses have status_code 200 instead of 5xx

                self.debug.error(ResponseConst.STATUS_CODE, status_code)
                self.debug.error(ResponseConst.RESPONSE, error_response)

                error_codes = ''.join([f'code {error[ResponseConst.CODE]}: '
                                       f'{error[ResponseConst.DETAIL]}'
                                       for error in error_response['errors']])

                msg = f'Request errors: {error_codes}'

                raise MarineTrafficRequestApiException(msg)
            else:
                self.debug.ok(ResponseConst.STATUS_CODE, status_code)
                self.debug.ok(ResponseConst.RESPONSE, response.raw_data)

            return response

        def call(self) -> 'Response':
            """
            Makes the API call
            :return: Return value from self._process_response()
            """

            self.url = self._prepare_url()
            status_code, response = self._do_request(self.url)
            return self._process_response(status_code, response)

    def call(client, *path_params, **query_params) -> Union['Response', None]:
        """
        Binded method for API calls
        :path_params: list of path parameters
        :query_params: dict of query parameters
        :return: Return value from ApiRequest.call()
        """

        if 'print_params' in query_params:
            ApiRequest.query_parameters.print_params()
            return

        with Debug(client=client) as debug:
            request = ApiRequest(client, debug, *path_params, **query_params)
            return request.call()

    call.__doc__ = request_data.get(ClientConst.DESCRIPTION)

    return call
