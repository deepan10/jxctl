import json
from mock import patch
import jenkins

import sys
sys.path.append("..")

#import unittest
#from jxctl.jxcore import pyjenkins
from .test_base import jxctlTestBase

class JenkinsListJobs(jxctlTestBase):
    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_all_jobs(self, mock_jobs):
        mock_jobs.return_value = self.jsons.all_jobs_json
        self.all_jobs = self.jxctl_context._list_all_jobs()
        self.assertCountEqual(self.all_jobs, self.jsons.all_jobs_return)
    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_jobs_exception(self, mock_jobs):
        mock_jobs.return_value = self.jsons.plugins_list
        with self.assertRaises(KeyError) as context_manager:
            self.jxctl_context._list_all_jobs()
        self.assertEqual(str(context_manager.exception), "'Key not found'")
        #self.assertRaises(KeyError, lambda: self.jxctl_context._list_all_jobs())

    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_mvn_pipe_jobs(self, mock_jobs):
        mock_jobs.return_value = self.jsons.all_jobs_json
        option_list = ['maven', 'pipeline']
        maven_pipeline_jobs = self.jxctl_context._list_jobs(option_list)
        self.assertCountEqual(maven_pipeline_jobs, self.jsons.maven_pipeline_return)
    
    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_free_jobs(self, mock_jobs):
        mock_jobs.return_value = self.jsons.all_jobs_json
        option_list = ['freestyle']
        freestyle_jobs = self.jxctl_context._list_jobs(option_list)
        self.assertCountEqual(freestyle_jobs, self.jsons.freestyle_jobs)
    
    @patch.object(jenkins.Jenkins, 'get_job_info')
    def test_job_info(self, mock_jobs):
        mock_jobs.return_value = self.jsons.job_info
        job_info_list = self.jxctl_context._job_info('test-pipeline-job')
        self.assertCountEqual(job_info_list, self.jsons.job_info_return)

    @patch.object(jenkins.Jenkins, 'get_build_info')
    def test_build_info(self, mock_build):
        mock_build.return_value = self.jsons.build_info
        build_info_list = self.jxctl_context._build_info('test-pipeline-job',10)
        self.assertCountEqual(build_info_list, self.jsons.build_info_return)
