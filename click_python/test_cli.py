import click
from testing import CliRunner
from simple_cli import main

# Unit test

def test_say_in_cli():
    runner = CliRunner()
    result = runner.invoke(main,['say','Hello'])
    assert 'you said Hello' in result.output
    assert result.exit_code == 0

def test_greet_in_cli():
    runner = CliRunner()
    result = runner.invoke(main,['greet','pranav'])
    assert 'Hello pra' in result.output
    assert result.exit_code == 0

