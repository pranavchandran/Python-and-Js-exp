import click

# @click.command()
# # @click.argument('name',default="python")
# @click.argument('number1',type=int)
# @click.argument('number2',type=int)
# @click.argument('method',default='sub')



# def main(number1,number2,method):
#     # click.echo('Hello {}'.format(name))
#     result = ''
#     if method == 'add':
#         result = (number1) + (number2)
#     elif method == 'substract':
#         result = (number1) - (number2)
#     elif method == 'multiply':
#         result = (number1) * (number2)
#         click.echo(result)
# i dont know it will not work
# def sub(num1,num2,method):
#     if method == 'sub':
#         result = int(num1)-int(num2)
#         click.echo(result)

@click.command()
@click.argument('source',nargs=-1)
@click.argument('destination',nargs=1)

def main(source,destination):
    for f in source:
        click.echo("Moving {} to Folder {}".format(f,destination))
        
    
    
if __name__ == "__main__":
    main()
