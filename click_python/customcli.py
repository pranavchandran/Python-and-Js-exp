import click

@click.command()
# basic options
@click.option('--name','-n',default = 'pranav',help='Firstname description')
# Multiple values
# @click.option('--name','-n',nargs=2)
@click.option('--salary','-s',nargs=2,help="Monthly Salary",type=int)
# Multiple options
@click.option('--location','-l',help="places you have visited",multiple=True)

def main(name,salary,location):
    click.echo('Hello world My name is {},My Salary is {}'.format(name,sum(salary)))
    click.echo('\n'.join(location))


if __name__ == "__main__":
    main()
