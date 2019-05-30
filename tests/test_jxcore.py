import unittest
from unittest import mock
from jxctl.jxcore import JxCore
from .support_json import SupportJSON

import jenkins
class JxCoreTest(unittest.TestCase):

    @mock.patch("builtins.exit")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_jxcore_init_exception(self, mock_jenkins, mock_ctxcore, mock_exit): 
        mock_jenkins.side_effect = jenkins.JenkinsException()
        mock_ctxcore.validate_context.return_value = True
        jxcore = JxCore()
        mock_exit.assert_called_once()
    
    @mock.patch("builtins.exit")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_jxcore_invalid_context(self, mock_jenkins, mock_ctxcore, mock_exit): 
        mock_jenkins.side_effect = jenkins.JenkinsException()
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_ctxcore_obj.validate_context.return_value = False
        jxcore = JxCore()
        mock_exit.assert_called_once()

    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_jobs_key_error(self, mock_jenkins, mock_ctxcore): 
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = [{"_class": "dummy"}]
        with self.assertRaises(KeyError) as context_manager:
            jxcore = JxCore()
            jxcore.list_all_jobs()
        self.assertEqual(str(context_manager.exception), "'Key not found'")

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_jobs_with_no_result(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = ""
        jxcore = JxCore()
        jxcore.list_all_jobs()
        expected_jobs_list = {"jobs": []}
        mock_print.assert_called_with(expected_jobs_list, "json", False)

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_jobs(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_all_jobs()
        expected_param = {"jobs" : [
            {"jobname": "maven-test-job", "joburl" : "http://localhost:8080/job/maven-test-job/"},
            {"jobname": "test-freestyle-job", "joburl" : "http://localhost:8080/job/test-freestyle-job/"},
            {"jobname": "pipeline-test-job", "joburl" : "http://localhost:8080/job/pipeline-test-job/"},
            {"jobname": "test-folder/test-sub-folder/subfolder-freestyle-job", "joburl" : "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/"}
            ]}
        mock_print.assert_called_with(expected_param, "json", False)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_jobs_count(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_all_jobs(count=True)
        expected_params = {"jobs" : [
            {"jobname": "maven-test-job", "joburl" : "http://localhost:8080/job/maven-test-job/"},
            {"jobname": "test-freestyle-job", "joburl" : "http://localhost:8080/job/test-freestyle-job/"},
            {"jobname": "pipeline-test-job", "joburl" : "http://localhost:8080/job/pipeline-test-job/"},
            {"jobname": "test-folder/test-sub-folder/subfolder-freestyle-job", "joburl" : "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/"}
        ]}
        mock_print.assert_called_with(expected_params, "json", True)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_jobs_with_option(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_jobs(["pipeline"])
        expected_params = {"jobs" : [
            {"jobname": "pipeline-test-job", "joburl": "http://localhost:8080/job/pipeline-test-job/"}
        ]}
        mock_print.assert_called_with(expected_params, "json", False)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_jobs_with_multi_option(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_jobs(["pipeline", "maven"])
        expected_params = {"jobs" : [
            {"jobname": "pipeline-test-job", "joburl" : "http://localhost:8080/job/pipeline-test-job/"},
            {"jobname": "maven-test-job", "joburl" : "http://localhost:8080/job/maven-test-job/"}
        ]}
        mock_print.assert_called_with(expected_params, "json", False)

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_plugins(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_plugins_info.return_value = SupportJSON().plugins_list
        jxcore = JxCore()
        jxcore.list_all_plugins()
        expected_plugins = SupportJSON().plugins_list_return
        mock_print.assert_called_with(expected_plugins, "json", False)

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_folders(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = SupportJSON().all_jobs_json
        jxcore = JxCore()
        jxcore.list_all_folders()
        expected_plugins = SupportJSON().folders_list_return
        mock_print.assert_called_with(expected_plugins, "json", False)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_folders_exception(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_all_jobs.return_value = [{'_class': 'com.cloudbees.hudson.plugins.folder.Folder'}]
        with self.assertRaises(KeyError) as context_manager:
            jxcore = JxCore()
            jxcore.list_all_folders()
        self.assertEqual(str(context_manager.exception), "'Key not found'")

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_list_all_plugins_with_count(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_plugins_info.return_value = SupportJSON().plugins_list
        jxcore = JxCore()
        jxcore.list_all_plugins(count=True)
        expected_plugin_list = SupportJSON().plugins_list_return
        mock_print.assert_called_with(expected_plugin_list, "json", True)

    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_job_info(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_job_info.return_value = SupportJSON().job_info
        jxcore = JxCore()
        jxcore.job_info("test-pipeline-job")
        expected_plugin_list = SupportJSON().job_info_return
        mock_print.assert_called_with(expected_plugin_list, "json")

    @mock.patch("time.ctime")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_build_info(self, mock_jenkins, mock_ctxcore, mock_print, mock_time):
        mock_time.return_value = "Fri Jul  3 11:10:41 50815"
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_build_info.return_value = SupportJSON().build_info
        jxcore = JxCore()
        jxcore.build_info("test-pipeline-job", "10")
        expected_build_info = SupportJSON().build_info_return
        mock_print.assert_called_with(expected_build_info, "json")

    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.build_job")
    def test_trigger_job(self, mock_jenkins, _):
        param = { "node" : "test" }
        jxcore = JxCore()
        jxcore.trigger_job("test_job", param)
        mock_jenkins.assert_called_with("test_job", param)
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.build_job")
    def test_trigger_job_exception(self, mock_jenkins, _):
        mock_jenkins.side_effect = jenkins.JenkinsException()
        param = { "node" : "test" }
        with self.assertRaises(jenkins.JenkinsException) as exception:
            jxcore = JxCore()
            jxcore.trigger_job("test_job", param)
        self.assertEqual(str(exception.exception), "Job not found")
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.stop_build")
    def test_abort_job(self, mock_jenkins, _):
        jxcore = JxCore()
        jxcore.abort_job("test_job", 10)
        mock_jenkins.assert_called_with("test_job", 10)
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.stop_build")
    def test_abort_job_exception(self, mock_jenkins, _):
        mock_jenkins.side_effect = jenkins.JenkinsException()
        with self.assertRaises(jenkins.JenkinsException) as exception:
            jxcore = JxCore()
            jxcore.abort_job("test_job", 10)
        self.assertEqual(str(exception.exception), "Job/Build not found")

    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.delete_job")
    def test_delete_job(self, mock_jenkins, _):
        jxcore = JxCore()
        jxcore.delete_job("test_job")
        mock_jenkins.assert_called_with("test_job")

    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.delete_job")
    def test_delete_job_exception(self, mock_jenkins, _):
        mock_jenkins.side_effect = jenkins.JenkinsException()
        with self.assertRaises(jenkins.JenkinsException) as exception:
            jxcore = JxCore()
            jxcore.delete_job("test_job")
        self.assertEqual(str(exception.exception), "Jenkins Exception")
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jenkins.Jenkins")
    def test_list_nodes(self, mock_jenkins, mock_print, mock_ctxcore):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_nodes.return_value = SupportJSON().list_nodes
        jxcore = JxCore()
        jxcore.list_nodes()
        expected_plugin_list = SupportJSON().list_nodes_return
        mock_print.assert_called_with(expected_plugin_list, "json", False)
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_node_info(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_node_info.return_value = SupportJSON().node_info
        jxcore = JxCore()
        jxcore.node_info("slave1")
        expected_plugin_list = SupportJSON().node_info_return
        mock_print.assert_called_with(expected_plugin_list, "json")
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_node_info_offline(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_node_info.return_value = SupportJSON().node_info_offline
        jxcore = JxCore()
        jxcore.node_info("slave1")
        expected_plugin_list = SupportJSON().node_info_offline_return
        mock_print.assert_called_with(expected_plugin_list, "json")
    
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins")
    def test_node_info_temp_offline(self, mock_jenkins, mock_ctxcore, mock_print):
        mock_ctxcore_obj = mock_ctxcore.return_value
        mock_server = mock_jenkins.return_value
        mock_ctxcore_obj.validate_context.return_value = True
        mock_server.get_node_info.return_value = SupportJSON().node_info_temp_offline
        jxcore = JxCore()
        jxcore.node_info("slave1")
        expected_plugin_list = SupportJSON().node_info_temp_offline_return
        mock_print.assert_called_with(expected_plugin_list, "json")
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.disable_node")
    def test_node_action_offline(self, mock_jenkins, _):
        jxcore = JxCore()
        jxcore.node_action("slave1", "offline")
        mock_jenkins.assert_called_with("slave1")
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.disable_node")
    def test_node_action_offline_msg(self, mock_jenkins, _):
        jxcore = JxCore()
        jxcore.node_action("slave1", "offline", "maintenance")
        mock_jenkins.assert_called_with("slave1", msg="maintenance")
    
    @mock.patch("jxctl.jxcore.CtxCore")
    @mock.patch("jenkins.Jenkins.enable_node")
    def test_node_action_online(self, mock_jenkins, _):
        jxcore = JxCore()
        jxcore.node_action("slave1", "online")
        mock_jenkins.assert_called_with("slave1")
