import click

@click.command()
@click.option('--name')
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True)


def main(name,password):
    fname = click.prompt("Enter your First name")
    click.echo(f'your name is {name} and your firsr name is {fname} and password is {password}')
    
if __name__ == "__main__":
    main()