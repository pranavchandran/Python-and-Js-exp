# pip install click_config_file

import click
import click_config_file

@click.command()
@click.option('--name','-n',default="Pranav",help="Specify Name")
@click.option('--salary','-s')
@click_config_file.configuration_option()
def main(name,salary):
    click.echo('Hello {} current sale is {}'.format(name,salary))


if __name__ == "__main__":
    main()