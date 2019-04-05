from collections import namedtuple


RequestConst = namedtuple('RequestConst',
                          ['GET',
                           'PATH',
                           'QUERY',
                           'METHOD',
                           'TIMEOUT',
                           'API_PATH',
                           'PROTOCOL',
                           'QUERY_PARAMETERS',
                           'DEFAULT_PARAMETERS'])('GET',
                                                  'path',
                                                  'query',
                                                  'method',
                                                  'timeout',
                                                  'api_path',
                                                  'protocol',
                                                  'query_parameters',
                                                  'default_parameters')

ResponseConst = namedtuple('ResponseConst',
                           ['CODE',
                            'DETAIL',
                            'TO_LIST',
                            'RESPONSE',
                            'STATUS_CODE',
                            'RESPONSE_OBJECT'])('code',
                                                'detail',
                                                'to_list',
                                                'response',
                                                'status_code',
                                                'response_object')

ClientConst = namedtuple('ClientConst',
                         ['META',
                          'MODEL',
                          'SIMPLE',
                          'MODELS',
                          'MSG_TYPE',
                          'FORMATTER',
                          'DESCRIPTION'])('meta',
                                          'model',
                                          'simple',
                                          'models',
                                          'msgtype',
                                          'formatter',
                                          'description')

FormatterConst = namedtuple('FormatterConst', ['XML',
                                               'CSV',
                                               'JSON',
                                               'JSONO',
                                               'FORMATTED'])('xml',
                                                             'csv',
                                                             'json',
                                                             'jsono',
                                                             'formatted')

TestConst = namedtuple('TestConst', ['FAKE_RESPONSE_PATH'])('fake_response_path')

ResponseCode = namedtuple('ResponseCode', ['OK', 'NOT_FOUND'])(200, 404)

BoolConst = namedtuple('BoolConst', ['TRUE', 'FALSE'])('1', '0')

MiscConst = namedtuple('MiscConst', ['ERRORS',
                                     'FORMAT',
                                     'PRINT_PARAMS'])('errors',
                                                      'format',
                                                      'print_params')

ResponseDataConst = namedtuple('ResponseDataConst', ['DATA',
                                                     'META',
                                                     'CODE',
                                                     'ERROR',
                                                     'STATUS',
                                                     'TOTAL_PAGES',
                                                     'DESCRIPTION',
                                                     'CURRENT_PAGE',
                                                     'TOTAL_RESULTS'])('DATA',
                                                                       'METADATA',
                                                                       'CODE',
                                                                       'ERROR',
                                                                       'STATUS',
                                                                       'TOTAL_PAGES',
                                                                       'DESCRIPTION',
                                                                       'CURRENT_PAGE',
                                                                       'TOTAL_RESULTS')
