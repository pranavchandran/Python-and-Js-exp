# Adding colors
# pip install colorama

import click


@click.command()
@click.option('--name','-n')
def main(name):
    # click.echo(click.style(('My name is {}'.format(name)),fg='red',bg='white',bold=True))
    click.secho(('My name is {}'.format(name)),fg='red',bg='white',bold=True)



if __name__ == "__main__":
    main()