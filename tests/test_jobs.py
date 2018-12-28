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
        mock_jobs.return_value = self.all_jobs_json
        all_jobs = self.jxctl_context._list_all_jobs()
        self.assertCountEqual(all_jobs, self.all_jobs_return)
    
    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_mvn_pipe_jobs(self, mock_jobs):
        mock_jobs.return_value = self.all_jobs_json
        option_list = ['maven', 'pipeline']
        maven_pipeline_jobs = self.jxctl_context._list_jobs(option_list)
        self.assertCountEqual(maven_pipeline_jobs, self.maven_pipeline_return)
    
    @patch.object(jenkins.Jenkins, 'get_all_jobs')
    def test_list_free_jobs(self, mock_jobs):
        mock_jobs.return_value = self.all_jobs_json
        option_list = ['freestyle']
        freestyle_jobs = self.jxctl_context._list_jobs(option_list)
        self.assertCountEqual(freestyle_jobs, self.freestyle_jobs)
    
    @patch.object(jenkins.Jenkins, 'get_job_info')
    def test_job_info(self, mock_jobs):
        mock_jobs.return_value = self.job_info
        job_info_list = self.jxctl_context._job_info('test-pipeline-job')
        self.assertListEqual(job_info_list, self.job_info_return)