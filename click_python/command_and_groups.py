    # reverse a sting
    # Leet conversion
    # Shuffling

import click
import random

@click.group()
def main():
    pass

@main.command()
@click.argument('text')
def reverse(text):
    '''reverse a text'''
    click.echo(text[::-1])

@main.command()
@click.argument('text')
def leet(text):
    '''leet a text'''
    chars = {'a':'4','b':'13','c':'','d':'[','e':'3','1':'1'}
    getchar = lambda c: chars[c] if c in chars else c
    click.echo(''.join(getchar(c)for c in text))

@main.command()
@click.argument('myword')
def shufflize(myword):
    '''Shuffle the text'''
    click.echo(''.join(random.sample(myword,len(myword))))

@main.command()
@click.argument('check')
def check_one(check):
    '''if it works'''
    click.echo(''.join(check)+'Genius mind hackers')



if __name__ == "__main__":
    main()