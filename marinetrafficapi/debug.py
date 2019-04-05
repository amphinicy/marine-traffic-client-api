import click
import pprint


STATUS_OK = 'ok'
STATUS_ERROR = 'error'


class Debug:

    def __init__(self, client):
        self.client = client
        self.recorded_data = {}

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.client.debug:
            self.standard_output()

    def ok(self, key, value):
        self.record(key, value, STATUS_OK)

    def error(self, key, value):
        self.record(key, value, STATUS_ERROR)

    def record(self, key, value, status):
        if self.client.debug:
            self.recorded_data[key] = {'value': value, 'status': status}

    def show(self, standard_output=False):
        if standard_output:
            self.standard_output()
        else:
            return self.recorded_data

    def standard_output(self):
        click.echo('')
        click.echo(click.style('Marine Traffic API Client Debug', fg='green'))
        click.echo(click.style('-'*100, fg='green'))

        for key, value in self.recorded_data.items():

            value = value['value']
            if type(value) == object:
                value = dir(value)

            output_str = '%s: [%s] %s' % (click.style(str(key), fg='green'),
                                          click.style(str(type(value)), fg='blue'),
                                          pprint.pformat(value))

            click.echo(output_str)
            click.echo(click.style('-'*100, fg='green'))

        click.echo('')
