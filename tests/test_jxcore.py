# from .test_base import jxctlTestBase
import unittest
from unittest import mock
from jxctl.jxcore import JxCore
from .support_json import SupportJSON

class JxCoreTest(unittest.TestCase):

    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_jobs_key_error(self, mock_jenkins, mock_ctxcore): 
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = [{"_class": "dummy"}]
        with self.assertRaises(KeyError) as context_manager:
            jxcore = JxCore()
            jxcore.list_all_jobs()
        self.assertEqual(str(context_manager.exception), "'Key not found'")

    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_jobs_with_no_result(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = ""
        jxcore = JxCore()
        jxcore.list_all_jobs()
        expected_jobs_list = []
        expected_table_header = ['Name', 'URL']
        mock_display.assert_called_with(expected_jobs_list, expected_table_header)

    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_jobs(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_all_jobs()
        expected_jobs_list = [['maven-test-job', 'http://localhost:8080/job/maven-test-job/'], ['test-freestyle-job', 'http://localhost:8080/job/test-freestyle-job/'], ['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/'], ['test-folder/test-sub-folder/subfolder-freestyle-job', 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/']]
        expected_table_header = ['Name', 'URL']
        mock_display.assert_called_with(expected_jobs_list, expected_table_header)
    
    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_jobs_count(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_all_jobs(count=True)
        expected_jobs_list = [['maven-test-job', 'http://localhost:8080/job/maven-test-job/'], ['test-freestyle-job', 'http://localhost:8080/job/test-freestyle-job/'], ['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/'], ['test-folder/test-sub-folder/subfolder-freestyle-job', 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/']]
        expected_table_header = ['No. of Jobs']
        mock_display.assert_called_with(expected_jobs_list, expected_table_header, count_flag=True)
    
    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_jobs_with_option(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_jobs(["pipeline"])
        expected_jobs_list = [['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/']]
        expected_table_header = ['Name', 'URL']
        mock_display.assert_called_with(expected_jobs_list, expected_table_header)
    
    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_jobs_with_multi_option(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_jobs(["pipeline", "maven"])
        expected_jobs_list = [['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/'], ['maven-test-job', 'http://localhost:8080/job/maven-test-job/']]
        expected_table_header = ['Name', 'URL']
        mock_display.assert_called_with(expected_jobs_list, expected_table_header)

    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_plugins(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_plugins_info.return_value = SupportJSON().plugins_list
        jxcore = JxCore()
        jxcore.list_all_plugins()
        expected_plugin_list = SupportJSON().plugins_list_return
        expected_table_header = ['Plugin Name', 'Short Name', 'Version']
        mock_display.assert_called_with(expected_plugin_list, expected_table_header)

    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_list_all_plugins_with_count(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_plugins_info.return_value = SupportJSON().plugins_list
        jxcore = JxCore()
        jxcore.list_all_plugins(count=True)
        expected_plugin_list = SupportJSON().plugins_list_return
        expected_table_header = ['No. of Plugins']
        mock_display.assert_called_with(expected_plugin_list, expected_table_header, True)

    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_job_info(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_job_info.return_value = SupportJSON().job_info
        jxcore = JxCore()
        jxcore.job_info("test-pipeline-job")
        expected_plugin_list = SupportJSON().job_info_return
        expected_table_header = ['Job Data', 'Detail']
        mock_display.assert_called_with(expected_plugin_list, expected_table_header)
    
    @mock.patch('jxctl.jxcore.JxCore.display_table')
    @mock.patch('jxctl.ctxcore.CtxCore')
    @mock.patch('jenkins.Jenkins')
    def test_build_info(self, mock_jenkins, mock_ctxcore, mock_display):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_build_info.return_value = SupportJSON().build_info
        jxcore = JxCore()
        jxcore.build_info("test-pipeline-job", "10")
        expected_plugin_list = SupportJSON().build_info_return
        expected_table_header = ["Build Data", "Detail"]
        mock_display.assert_called_with(expected_plugin_list, expected_table_header)