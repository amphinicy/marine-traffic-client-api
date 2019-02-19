import requests
from typing import TYPE_CHECKING

from marinetrafficapi.debug import Debug
from marinetrafficapi.formatter import FormatterFactory
from marinetrafficapi.exceptions import MarineTrafficRequestApiException
from marinetrafficapi.reponse import Response

if TYPE_CHECKING:
    from marinetrafficapi.client import Client


def bind_request(**request_data) -> 'callable':
    """Binds request class to client property, dynamically."""

    class ApiRequest(object):
        """Request class. Does the actual API request."""

        model = request_data.get('model')
        api_path = request_data.get('api_path')
        method = request_data.get('method', 'GET')
        query_parameters = request_data.get('query_parameters')
        default_parameters = request_data.get('default_parameters')
        fake_response_path = request_data.get('fake_response_path')

        def __init__(self, client: 'Client', debug: 'Debug',
                     *path_params, **query_params):
            client.request = self

            self.url = None
            self.debug = debug
            self.client = client
            self.parameters = {'query': {}, 'path': []}

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
                self._timeout = int(query_params.get('timeout', self._timeout))
            except ValueError:
                pass
            try:
                del query_params['timeout']
            except KeyError:
                pass

            # set default API call params
            for key, value in self.default_parameters.items():
                self.parameters['query'][key] = value  # str(value).encode('utf-8')

            # set API call params defined during the "call" invocation
            for key, value in query_params.items():
                if value is None:
                    continue

                query_params = self.query_parameters.get_params()

                if key in query_params.values():
                    self.parameters['query'][key] = value  # str(value).encode('utf-8')

                elif key in query_params.keys():
                    self.parameters['query'][query_params[key]] = \
                        value  # str(value).encode('utf-8')

            # transform all True and False param to 1 and 0
            for key, value in self.parameters['query'].items():
                if value is True:
                    self.parameters['query'][key] = '1'
                if value is False:
                    self.parameters['query'][key] = '0'

            # set optional url path params
            for value in path_params:
                self.parameters['path'].append(value.encode('utf-8'))

        def _prepare_url(self) -> str:
            """
            Prepares url and query parameters for the request
            :return: URL
            """

            url_parts = {
                'protocol': self.client.protocol,
                'base_url': self.client.base_url,
                'base_path': self.client.base_path,
                'api_path': self.api_path,
                'api_key': self.client.api_key
            }
            url = '{protocol}://{base_url}{base_path}{api_path}/{api_key}'\
                .format(**url_parts)

            url_parts = self.parameters['path']
            url_parts.insert(0, url)

            url = '/'.join([part if type(part) == str else
                            part.decode('utf-8') for part in url_parts])

            self.debug.ok('url', url)
            self.debug.ok('query_parameters', self.parameters['query'])

            url = '{}/{}'.format(url, '/'.join(['{}:{}'.format(key, value)
                                                for key, value in
                                                self.parameters['query'].items()]))
            self.debug.ok('final url', url)

            return url

        def _do_request(self, url: str) -> (int, dict):
            """
            Makes the request to Marine Traffic Api servers
            :url: Url for the request
            :return: Tuple with two elements, status code and content
            """

            if self.client.fake_response_path:
                with open(self.client.fake_response_path, 'r') as f:
                    return 200, f.read()

            elif self.method == 'GET':
                response = requests.get(url, timeout=self._timeout)
                self.debug.ok('response_object', response)
                return response.status_code, response.text

            else:
                # For future POST, PUT, DELETE requests
                return 404, {}

        def _process_response(self, status_code: int, response: str) -> 'Response':
            """
            Process response using models
            :status_code: Response status code
            :response: Content
            :return: Response object
            """

            formatter = FormatterFactory(self.parameters['query']['protocol'])\
                .get_formatter()

            response = Response(response, status_code, formatter, self)

            error_response = response.to_list
            if 'errors' in error_response:
                # error responses have status_code 200 instead of 5xx

                self.debug.error('status_code', status_code)
                self.debug.error('response', error_response)

                msg = 'Request errors: {}'.format(''.join(
                    ['code {}: {}'.format(error['code'], error['detail'])
                     for error in error_response['errors']]))

                raise MarineTrafficRequestApiException(msg)
            else:
                self.debug.ok('status_code', status_code)
                self.debug.ok('response', response.raw_data)

            return response

        def call(self) -> 'Response':
            """
            Makes the API call
            :return: Return value from self._process_response()
            """

            self.url = self._prepare_url()
            status_code, response = self._do_request(self.url)
            return self._process_response(status_code, response)

    def call(client, *path_params, **query_params) -> 'Response':
        """
        Binded method for API calls
        :path_params: list of path parameters
        :query_params: dict of query parameters
        :return: Return value from ApiRequest.call()
        """

        with Debug(client=client) as debug:
            request = ApiRequest(client, debug, *path_params, **query_params)
            return request.call()

    return call
