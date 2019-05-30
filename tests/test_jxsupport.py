import unittest
from unittest import mock
from jxctl.jxsupport import JxSupport
from .support_json import SupportJSON

class TestJxSupport(unittest.TestCase):

    @mock.patch("jxctl.jxsupport.JxSupport.print_json")
    def test_print_with_json(self, mock_print):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print(source_dict, format_display="json")
        mock_print.assert_called_with(source_dict, False)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print_table")
    def test_print_with_table(self, mock_print):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print(source_dict, format_display="table")
        mock_print.assert_called_with(source_dict, False)
    
    @mock.patch("jxctl.jxsupport.tabulate")
    def test_print_table(self, mock_tabulate):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print_table(source_dict,False)
        expected_table = [['master', 'Online'], ['slave1', 'Online']]
        expected_header = ['nodename', 'status']
        mock_tabulate.assert_called_with(expected_table, headers=expected_header, tablefmt='orgtbl')

    @mock.patch("jxctl.jxsupport.tabulate")
    def test_print_table_with_count(self, mock_tabulate):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print_table(source_dict,True)
        expected_table = [[2]]
        expected_header = ['nodes']
        mock_tabulate.assert_called_with(expected_table, headers=expected_header, tablefmt='orgtbl')
    
    @mock.patch("pprint.pprint")
    def test_print_json(self, mock_pprint):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print_json(source_dict,False)
        mock_pprint.assert_called_with(source_dict)
    
    @mock.patch("pprint.pprint")
    def test_print_json_with_count(self, mock_pprint):
        source_dict = {
            'nodes': [{
                'nodename': 'master',
                'status': 'Online'
                },
                {
                'nodename': 'slave1',
                'status': 'Online'
                }
            ]}
        test_obj = JxSupport()
        test_obj.print_json(source_dict,True)
        expected_dict = {'nodes': 2}
        mock_pprint.assert_called_with(expected_dict)


        