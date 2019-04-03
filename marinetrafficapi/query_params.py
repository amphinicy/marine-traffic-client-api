import click
from typing import Dict
from dumpit import pdumpit
from aenum import MultiValueEnum


class DefaultQueryParams(MultiValueEnum):
    """Default set of query parameters."""

    msg_type = 'msgtype', 'simple or extended (extended cost more credits)'
    protocol = 'protocol', 'Response type. Use one of the following: '\
                           'xml, csv, json, jsono (object)'


class QueryParams(MultiValueEnum):
    """Query parameters for API calls."""

    @classmethod
    def get_params(cls) -> Dict:
        """Merges default query parameters with call specific query parameters."""

        return {**{param.name: param.value for param in cls},
                **{param.name: param.value for param in DefaultQueryParams}}

    @classmethod
    def print_params(cls) -> None:
        """Prints all query parameters."""

        for param in DefaultQueryParams:
            param.__doc__ = param.values[1]

        click.echo('Default params:')
        pdumpit(DefaultQueryParams, all_=False)

        for param in cls:
            param.__doc__ = param.values[1]

        click.echo(f'{cls.__name__} params:')
        pdumpit(cls, all_=False)
