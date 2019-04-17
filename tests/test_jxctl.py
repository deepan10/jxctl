
import click
from click.testing import CliRunner
import unittest
from unittest import mock
from jxctl import cli

class TestJxCtl(unittest.TestCase):

    @mock.patch('jxctl.jxcore.JxCore.list_all_plugins')
    def test_info(self, mock_plugins):
        mock_plugins.return_value = False
        runner = CliRunner()
        result = runner.invoke(cli.plugins)
        assert result.exit_code == 0
        
        