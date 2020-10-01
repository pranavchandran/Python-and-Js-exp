#!/usr/bin/env python
import click

@click.command()
def cli():
    """Example script."""
    click.echo('pip3 install')

# --editable option requires 1 argument
# error solved by 
# pip install -e .