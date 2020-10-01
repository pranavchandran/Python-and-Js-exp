import click
from click_params import EMAIL,PUBLIC_URL,DOMAINS

@click.group()
def main():
    pass

@main.command()
@click.option('--name','-n')
@click.option('--email','-e',type=EMAIL)
@click.option('--domain','-d',type=DOMAINS)
@click.option('--website','-w',type=PUBLIC_URL)


def add_user(name,email,domain,website):
    click.secho('your name is {}'.format(name.title()))
    click.secho('your email is {}'.format(email),fg='green')
    click.secho('your domain is {}'.format(domain))
    click.secho('your website is {}'.format(website),fg='green')

if __name__ == "__main__":
    main()