import click

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The ')

# @click.option('--mobile', prompt='Mobile',
#               help='The ')
# def hello(count, name,mobile):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#         click.echo('Number is %s!'% mobile)


# if __name__ == '__main__':
#     hello()

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()  # @cli, not @click!
def sync():
    click.echo('Syncing')
