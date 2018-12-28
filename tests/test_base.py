import json
import mock
from mock import patch
import jenkins


import sys
sys.path.append("..")

import unittest
from jxctl.jxcore import pyjenkins
from jxctl.ctlcore import ctlCore

class jxctlTestBase(unittest.TestCase):
    def load_JSONS(self):
        self.all_jobs_json = [{
            '_class': 'hudson.maven.MavenModuleSet',
            'name': 'maven-test-job',
            'url': 'http://localhost:8080/job/maven-test-job/',
            'color': 'blue',
            'fullname': 'maven-test-job'
            }, {
                '_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                'name': 'test-folder',
                'url': 'http://localhost:8080/job/test-folder/',
                'jobs': [{
                    '_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                    'name': 'test-sub-folder',
                    'url': 'http://localhost:8080/job/test-folder/job/test-sub-folder/',
                    'jobs': [{
                        '_class': 'hudson.model.FreeStyleProject',
                        'name': 'subfolder-freestyle-job',
                        'url': 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/',
                        'color': 'notbuilt',
                        'fullname': 'test-folder/test-sub-folder/subfolder-freestyle-job'
                    }],
                'fullname': 'test-folder/test-sub-folder'
                }],
                'fullname': 'test-folder'
            }, {
                '_class': 'hudson.model.FreeStyleProject',
                'name': 'test-freestyle-job',
                'url': 'http://localhost:8080/job/test-freestyle-job/',
                'color': 'notbuilt',
                'fullname': 'test-freestyle-job'
            }, {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'name': 'pipeline-test-job',
                'url': 'http://localhost:8080/job/pipeline-test-job/',
                'color': 'red',
                'fullname': 'pipeline-test-job'
            }, {
                '_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                'name': 'test-sub-folder',
                'url': 'http://localhost:8080/job/test-folder/job/test-sub-folder/',
                'jobs': [{
                    '_class': 'hudson.model.FreeStyleProject',
                    'name': 'subfolder-freestyle-job',
                    'url': 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/',
                    'color': 'notbuilt',
                    'fullname': 'test-folder/test-sub-folder/subfolder-freestyle-job'
                }],
                'fullname': 'test-folder/test-sub-folder'
            }, {
                '_class': 'hudson.model.FreeStyleProject',
                'name': 'subfolder-freestyle-job',
                'url': 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/',
                'color': 'notbuilt',
                'fullname': 'test-folder/test-sub-folder/subfolder-freestyle-job'
            }]

        self.all_jobs_return = [
                ['maven-test-job', 'http://localhost:8080/job/maven-test-job/'],
                ['test-freestyle-job', 'http://localhost:8080/job/test-freestyle-job/'], 
                ['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/'],
                ['test-folder/test-sub-folder/subfolder-freestyle-job', 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/']
            ]
        
        self.maven_pipeline_return = [
                ['maven-test-job', 'http://localhost:8080/job/maven-test-job/'],
                ['pipeline-test-job', 'http://localhost:8080/job/pipeline-test-job/']
            ]
        
        self.freestyle_jobs = [
                ['test-freestyle-job', 'http://localhost:8080/job/test-freestyle-job/'], 
                ['test-folder/test-sub-folder/subfolder-freestyle-job', 'http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/']
            ]

        self.plugins_list = [{
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'Folders Plugin',
                'pinned': False,
                'requiredCoreVersion': '2.60.3',
                'shortName': 'cloudbees-folder',
                'supportsDynamicLoad': 'MAYBE',
                'url': 'https://wiki.jenkins.io/display/JENKINS/CloudBees+Folders+Plugin',
                'version': 6.5
            }, {
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'Structs Plugin',
                'pinned': False,
                'requiredCoreVersion': '2.60.3',
                'shortName': 'structs',
                'supportsDynamicLoad': 'MAYBE',
                'url': 'https://wiki.jenkins-ci.org/display/JENKINS/Structs+plugin',
                'version': 1.17
            }, {
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'bouncycastle API Plugin',
                'pinned': False,
                'requiredCoreVersion': '2.60.3',
                'shortName': 'bouncycastle-api',
                'supportsDynamicLoad': 'YES',
                'url': 'http://wiki.jenkins-ci.org/display/JENKINS/Bouncy+Castle+API+Plugin',
                'version': 2.17
            }, {
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [{
                    'optional': False,
                    'shortName': 'bouncycastle-api',
                    'version': '2.16.0'
                }],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'Script Security Plugin',
                'pinned': False,
                'requiredCoreVersion': '2.7.3',
                'shortName': 'script-security',
                'supportsDynamicLoad': 'MAYBE',
                'url': 'https://wiki.jenkins.io/display/JENKINS/Script+Security+Plugin',
                'version': 1.49
            }, {
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [{
                    'optional': False,
                    'shortName': 'structs',
                    'version': '1.5'
                }, {
                    'optional': False,
                    'shortName': 'bouncycastle-api',
                    'version': '2.16.0'
                }],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'Pipeline: Step API',
                'pinned': False,
                'requiredCoreVersion': '1.642.3',
                'shortName': 'workflow-step-api',
                'supportsDynamicLoad': 'YES',
                'url': 'https://wiki.jenkins-ci.org/display/JENKINS/Pipeline+Step+API+Plugin',
                'version': 2.17
            }, {
                'active': True,
                'backupVersion': None,
                'bundled': False,
                'deleted': False,
                'dependencies': [{
                    'optional': False,
                    'shortName': 'structs',
                    'version': '1.9'
                }, {
                    'optional': False,
                    'shortName': 'bouncycastle-api',
                    'version': '2.16.0'
                }],
                'downgradable': False,
                'enabled': True,
                'hasUpdate': False,
                'longName': 'SCM API Plugin',
                'pinned': False,
                'requiredCoreVersion': '2.7.3',
                'shortName': 'scm-api',
                'supportsDynamicLoad': 'MAYBE',
                'url': 'http://wiki.jenkins-ci.org/display/JENKINS/SCM+API+Plugin',
                'version': 2.3
            }]

        self.plugins_list_return = [
                ['Folders Plugin', 'cloudbees-folder', 6.5],
                ['Structs Plugin', 'structs', 1.17],
                ['bouncycastle API Plugin', 'bouncycastle-api', 2.17],
                ['Script Security Plugin', 'script-security', 1.49],
                ['Pipeline: Step API', 'workflow-step-api', 2.17],
                ['SCM API Plugin', 'scm-api', 2.3]
            ]
        
        self.job_info = {
            '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
            'actions': [{}, {}, {}, {}, {}, {}, {}, {}, {}, {
                '_class': 'com.cloudbees.plugins.credentials.ViewCredentialsAction'
            }],
            'description': '',
            'displayName': 'test-pipeline-job',
            'displayNameOrNull': None,
            'fullDisplayName': 'test-pipeline-job',
            'fullName': 'test-pipeline-job',
            'name': 'test-pipeline-job',
            'url': 'http://localhost:8080/job/test-pipeline-job/',
            'buildable': True,
            'builds': [{
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 5,
                'url': 'http://localhost:8080/job/test-pipeline-job/5/'
            }, {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 4,
                'url': 'http://localhost:8080/job/test-pipeline-job/4/'
            }, {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 3,
                'url': 'http://localhost:8080/job/test-pipeline-job/3/'
            }, {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 2,
                'url': 'http://localhost:8080/job/test-pipeline-job/2/'
            }, {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 1,
                'url': 'http://localhost:8080/job/test-pipeline-job/1/'
            }],
            'color': 'blue',
            'firstBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 1,
                'url': 'http://localhost:8080/job/test-pipeline-job/1/'
            },
            'healthReport': [{
                'description': 'Build stability: 2 out of the last 5 builds failed.',
                'iconClassName': 'icon-health-40to59',
                'iconUrl': 'health-40to59.png',
                'score': 60
            }],
            'inQueue': False,
            'keepDependencies': False,
            'lastBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 5,
                'url': 'http://localhost:8080/job/test-pipeline-job/5/'
            },
            'lastCompletedBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 5,
                'url': 'http://localhost:8080/job/test-pipeline-job/5/'
            },
            'lastFailedBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 2,
                'url': 'http://localhost:8080/job/test-pipeline-job/2/'
            },
            'lastStableBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 5,
                'url': 'http://localhost:8080/job/test-pipeline-job/5/'
            },
            'lastSuccessfulBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 5,
                'url': 'http://localhost:8080/job/test-pipeline-job/5/'
            },
            'lastUnstableBuild': None,
            'lastUnsuccessfulBuild': {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowRun',
                'number': 2,
                'url': 'http://localhost:8080/job/test-pipeline-job/2/'
            },
            'nextBuildNumber': 6,
            'property': [],
            'queueItem': None,
            'concurrentBuild': True,
            'resumeBlocked': False
        }

        self.job_info_return = [
                ['Name', 'test-pipeline-job'], 
                ['URL', 'http://localhost:8080/job/test-pipeline-job/'], 
                ['Type', 'org.jenkinsci.plugins.workflow.job.WorkflowJob'], 
                ['Last Completed Build', [5]], 
                ['Last Sucessful Build', [5]], 
                ['Last Build', [5]], 
                ['Builds', [5, 4, 3, 2, 1]]
            ]
    @patch.object(ctlCore, 'validate_context')
    def init_pyjenkins(self, mocl_context=False):
        mocl_context.return_value = True
        self.jxctl_context = pyjenkins()
    
    def setUp(self):
        super(jxctlTestBase, self).setUp()
        self.init_pyjenkins()
        self.load_JSONS()

    def tearDown(self):
        pass

