class SupportJSON():
    """
    Support Jenkins API JSON for testing
    """
    def __init__(self):
        self.all_jobs_json = [{
            "_class": "hudson.maven.MavenModuleSet",
            "name": "maven-test-job",
            "url": "http://localhost:8080/job/maven-test-job/",
            "color": "blue",
            "fullname": "maven-test-job"
            }, {
                "_class": "com.cloudbees.hudson.plugins.folder.Folder",
                "name": "test-folder",
                "url": "http://localhost:8080/job/test-folder/",
                "jobs": [{
                    "_class": "com.cloudbees.hudson.plugins.folder.Folder",
                    "name": "test-sub-folder",
                    "url": "http://localhost:8080/job/test-folder/job/test-sub-folder/",
                    "jobs": [{
                        "_class": "hudson.model.FreeStyleProject",
                        "name": "subfolder-freestyle-job",
                        "url": "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/",
                        "color": "notbuilt",
                        "fullname": "test-folder/test-sub-folder/subfolder-freestyle-job"
                    }],
                "fullname": "test-folder/test-sub-folder"
                }],
                "fullname": "test-folder"
            }, {
                "_class": "hudson.model.FreeStyleProject",
                "name": "test-freestyle-job",
                "url": "http://localhost:8080/job/test-freestyle-job/",
                "color": "notbuilt",
                "fullname": "test-freestyle-job"
            }, {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
                "name": "pipeline-test-job",
                "url": "http://localhost:8080/job/pipeline-test-job/",
                "color": "red",
                "fullname": "pipeline-test-job"
            }, {
                "_class": "com.cloudbees.hudson.plugins.folder.Folder",
                "name": "test-sub-folder",
                "url": "http://localhost:8080/job/test-folder/job/test-sub-folder/",
                "jobs": [{
                    "_class": "hudson.model.FreeStyleProject",
                    "name": "subfolder-freestyle-job",
                    "url": "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/",
                    "color": "notbuilt",
                    "fullname": "test-folder/test-sub-folder/subfolder-freestyle-job"
                }],
                "fullname": "test-folder/test-sub-folder"
            }, {
                "_class": "hudson.model.FreeStyleProject",
                "name": "subfolder-freestyle-job",
                "url": "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/",
                "color": "notbuilt",
                "fullname": "test-folder/test-sub-folder/subfolder-freestyle-job"
            }]

        self.all_jobs_return = [
                ["maven-test-job", "http://localhost:8080/job/maven-test-job/"],
                ["test-freestyle-job", "http://localhost:8080/job/test-freestyle-job/"], 
                ["pipeline-test-job", "http://localhost:8080/job/pipeline-test-job/"],
                ["test-folder/test-sub-folder/subfolder-freestyle-job", "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/"]
            ]
        
        self.maven_pipeline_return = [
                ["maven-test-job", "http://localhost:8080/job/maven-test-job/"],
                ["pipeline-test-job", "http://localhost:8080/job/pipeline-test-job/"]
            ]
        
        self.freestyle_jobs = [
                ["test-freestyle-job", "http://localhost:8080/job/test-freestyle-job/"], 
                ["test-folder/test-sub-folder/subfolder-freestyle-job", "http://localhost:8080/job/test-folder/job/test-sub-folder/job/subfolder-freestyle-job/"]
            ]

        self.plugins_list = [{
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "Folders Plugin",
                "pinned": False,
                "requiredCoreVersion": "2.60.3",
                "shortName": "cloudbees-folder",
                "supportsDynamicLoad": "MAYBE",
                "url": "https://wiki.jenkins.io/display/JENKINS/CloudBees+Folders+Plugin",
                "version": 6.5
            }, {
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "Structs Plugin",
                "pinned": False,
                "requiredCoreVersion": "2.60.3",
                "shortName": "structs",
                "supportsDynamicLoad": "MAYBE",
                "url": "https://wiki.jenkins-ci.org/display/JENKINS/Structs+plugin",
                "version": 1.17
            }, {
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "bouncycastle API Plugin",
                "pinned": False,
                "requiredCoreVersion": "2.60.3",
                "shortName": "bouncycastle-api",
                "supportsDynamicLoad": "YES",
                "url": "http://wiki.jenkins-ci.org/display/JENKINS/Bouncy+Castle+API+Plugin",
                "version": 2.17
            }, {
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [{
                    "optional": False,
                    "shortName": "bouncycastle-api",
                    "version": "2.16.0"
                }],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "Script Security Plugin",
                "pinned": False,
                "requiredCoreVersion": "2.7.3",
                "shortName": "script-security",
                "supportsDynamicLoad": "MAYBE",
                "url": "https://wiki.jenkins.io/display/JENKINS/Script+Security+Plugin",
                "version": 1.49
            }, {
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [{
                    "optional": False,
                    "shortName": "structs",
                    "version": "1.5"
                }, {
                    "optional": False,
                    "shortName": "bouncycastle-api",
                    "version": "2.16.0"
                }],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "Pipeline: Step API",
                "pinned": False,
                "requiredCoreVersion": "1.642.3",
                "shortName": "workflow-step-api",
                "supportsDynamicLoad": "YES",
                "url": "https://wiki.jenkins-ci.org/display/JENKINS/Pipeline+Step+API+Plugin",
                "version": 2.17
            }, {
                "active": True,
                "backupVersion": None,
                "bundled": False,
                "deleted": False,
                "dependencies": [{
                    "optional": False,
                    "shortName": "structs",
                    "version": "1.9"
                }, {
                    "optional": False,
                    "shortName": "bouncycastle-api",
                    "version": "2.16.0"
                }],
                "downgradable": False,
                "enabled": True,
                "hasUpdate": False,
                "longName": "SCM API Plugin",
                "pinned": False,
                "requiredCoreVersion": "2.7.3",
                "shortName": "scm-api",
                "supportsDynamicLoad": "MAYBE",
                "url": "http://wiki.jenkins-ci.org/display/JENKINS/SCM+API+Plugin",
                "version": 2.3
            }]

        self.plugins_list_return = {"plugins" : [
                {"pluginname" : "Folders Plugin", "pluginkey" : "cloudbees-folder", "version" : 6.5},
                {"pluginname" : "Structs Plugin", "pluginkey" : "structs", "version" : 1.17},
                {"pluginname" : "bouncycastle API Plugin", "pluginkey" : "bouncycastle-api", "version" : 2.17},
                {"pluginname" : "Script Security Plugin", "pluginkey" : "script-security", "version" : 1.49},
                {"pluginname" : "Pipeline: Step API", "pluginkey" : "workflow-step-api", "version" : 2.17},
                {"pluginname" : "SCM API Plugin", "pluginkey" : "scm-api", "version" : 2.3}
            ]}

        self.folders_list = [
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'red',
                'fullname': 'dnotifica',
                'name': 'dnotifica',
                'url': 'http://localhost:8080/job/dnotifica/'},
            {
                '_class': 'hudson.maven.MavenModuleSet',
                'color': 'blue',
                'fullname': 'dnotifica-mvn',
                'name': 'dnotifica-mvn',
                'url': 'http://localhost:8080/job/dnotifica-mvn/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'blue',
                'fullname': 'dnotifica-pipe',
                'name': 'dnotifica-pipe',
                'url': 'http://localhost:8080/job/dnotifica-pipe/'},
            {
                '_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                'fullname': 'folder1',
                'jobs': [{'_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                            'fullname': 'folder1/sub_folder1',
                            'jobs': [{'_class': 'hudson.model.FreeStyleProject',
                                    'color': 'blue',
                                    'fullname': 'folder1/sub_folder1/test',
                                    'name': 'test',
                                    'url': 'http://localhost:8080/job/folder1/job/sub_folder1/job/test/'}],
                            'name': 'sub_folder1',
                            'url': 'http://localhost:8080/job/folder1/job/sub_folder1/'}],
                'name': 'folder1',
                'url': 'http://localhost:8080/job/folder1/'},
            {
                '_class': 'hudson.model.FreeStyleProject',
                'color': 'notbuilt',
                'fullname': 'free_style_1',
                'name': 'free_style_1',
                'url': 'http://localhost:8080/job/free_style_1/'},
            {
                '_class': 'hudson.maven.MavenModuleSet',
                'color': 'notbuilt',
                'fullname': 'maven_test1',
                'name': 'maven_test1',
                'url': 'http://localhost:8080/job/maven_test1/'},
            {
                '_class': 'hudson.model.FreeStyleProject',
                'color': 'blue',
                'fullname': 'pytest',
                'name': 'pytest',
                'url': 'http://localhost:8080/job/pytest/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'blue',
                'fullname': 'slack-item',
                'name': 'slack-item',
                'url': 'http://localhost:8080/job/slack-item/'},
            {
                '_class': 'hudson.maven.MavenModuleSet',
                'color': 'blue',
                'fullname': 'smp_test',
                'name': 'smp_test',
                'url': 'http://localhost:8080/job/smp_test/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'red',
                'fullname': 'test-dsl',
                'name': 'test-dsl',
                'url': 'http://localhost:8080/job/test-dsl/'},
            {
                '_class': 'hudson.model.FreeStyleProject',
                'color': 'blue',
                'fullname': 'test-logstash',
                'name': 'test-logstash',
                'url': 'http://localhost:8080/job/test-logstash/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'blue',
                'fullname': 'test-pipe-lib',
                'name': 'test-pipe-lib',
                'url': 'http://localhost:8080/job/test-pipe-lib/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'blue',
                'fullname': 'test-pipe-logstash',
                'name': 'test-pipe-logstash',
                'url': 'http://localhost:8080/job/test-pipe-logstash/'},
            {
                '_class': 'org.jenkinsci.plugins.workflow.job.WorkflowJob',
                'color': 'blue',
                'fullname': 'test_pipeline',
                'name': 'test_pipeline',
                'url': 'http://localhost:8080/job/test_pipeline/'},
            {
                '_class': 'com.cloudbees.hudson.plugins.folder.Folder',
                'fullname': 'folder1/sub_folder1',
                'jobs': [{'_class': 'hudson.model.FreeStyleProject',
                            'color': 'blue',
                            'fullname': 'folder1/sub_folder1/test',
                            'name': 'test',
                            'url': 'http://localhost:8080/job/folder1/job/sub_folder1/job/test/'}],
                'name': 'sub_folder1',
                'url': 'http://localhost:8080/job/folder1/job/sub_folder1/'},
            {
                '_class': 'hudson.model.FreeStyleProject',
                'color': 'blue',
                'fullname': 'folder1/sub_folder1/test',
                'name': 'test',
                'url': 'http://localhost:8080/job/folder1/job/sub_folder1/job/test/'}
        ]

        self.folders_list_return = {
            'folders': [
                {
                    'foldername': 'test-folder',
                    'folderurl': 'http://localhost:8080/job/test-folder/'
                },
                {
                    'foldername': 'test-folder/test-sub-folder',
                    'folderurl': 'http://localhost:8080/job/test-folder/job/test-sub-folder/'
                }
            ]
        }
        
        self.job_info = {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "actions": [{}, {}, {}, {}, {}, {}, {}, {}, {}, {
                "_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"
            }],
            "description": "",
            "displayName": "test-pipeline-job",
            "displayNameOrNull": None,
            "fullDisplayName": "test-pipeline-job",
            "fullName": "test-pipeline-job",
            "name": "test-pipeline-job",
            "url": "http://localhost:8080/job/test-pipeline-job/",
            "buildable": True,
            "builds": [{
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 5,
                "url": "http://localhost:8080/job/test-pipeline-job/5/"
            }, {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 4,
                "url": "http://localhost:8080/job/test-pipeline-job/4/"
            }, {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 3,
                "url": "http://localhost:8080/job/test-pipeline-job/3/"
            }, {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 2,
                "url": "http://localhost:8080/job/test-pipeline-job/2/"
            }, {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/test-pipeline-job/1/"
            }],
            "color": "blue",
            "firstBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/test-pipeline-job/1/"
            },
            "healthReport": [{
                "description": "Build stability: 2 out of the last 5 builds failed.",
                "iconClassName": "icon-health-40to59",
                "iconUrl": "health-40to59.png",
                "score": 60
            }],
            "inQueue": False,
            "keepDependencies": False,
            "lastBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 5,
                "url": "http://localhost:8080/job/test-pipeline-job/5/"
            },
            "lastCompletedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 5,
                "url": "http://localhost:8080/job/test-pipeline-job/5/"
            },
            "lastFailedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 2,
                "url": "http://localhost:8080/job/test-pipeline-job/2/"
            },
            "lastStableBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 5,
                "url": "http://localhost:8080/job/test-pipeline-job/5/"
            },
            "lastSuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 5,
                "url": "http://localhost:8080/job/test-pipeline-job/5/"
            },
            "lastUnstableBuild": None,
            "lastUnsuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 2,
                "url": "http://localhost:8080/job/test-pipeline-job/2/"
            },
            "nextBuildNumber": 6,
            "property": [],
            "queueItem": None,
            "concurrentBuild": True,
            "resumeBlocked": False
        }

        self.job_info_return = {
            "test-pipeline-job" : [{
                "Name": "test-pipeline-job",
                "URL": "http://localhost:8080/job/test-pipeline-job/",
                "Type": "pipeline",
                "Last Completed Build": 5,
                "Last Sucessful Build": 5,
                "Last Build": 5
            }]
        }

        self.build_info ={
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
            "actions": [{
                "_class": "hudson.model.CauseAction",
                "causes": [{
                    "_class": "hudson.model.Cause$UserIdCause",
                    "shortDescription": "Started by user admin",
                    "userId": "admin",
                    "userName": "admin"
                }]
            }, {}, {}, {}, {}, {}, {}, {}, {}, {
                "_class": "org.jenkinsci.plugins.workflow.job.views.FlowGraphAction"
            }, {}, {}],
            "artifacts": [],
            "building": False,
            "description": None,
            "displayName": "#10",
            "duration": 9359,
            "estimatedDuration": 22407,
            "executor": None,
            "fullDisplayName": "test-pipeline-job #10",
            "id": "10",
            "keepLog": False,
            "number": 10,
            "queueId": 15,
            "result": "FAILURE",
            "timestamp": 1541415172241,
            "url": "http://localhost:8080/job/test-pipeline-job/10/",
            "changeSets": [],
            "culprits": [{
                "absoluteUrl": "http://localhost:8080/user/unknown",
                "fullName": "unknown"
            }],
            "nextBuild": {
                "number": 11,
                "url": "http://localhost:8080/job/test-pipeline-job/11/"
            },
            "previousBuild": {
                "number": 9,
                "url": "http://localhost:8080/job/test-pipeline-job/9/"
            }
        }

        self.build_info_return = {
            "test-pipeline-job": [{
                "Build No.": "10",
                "URL": "http://localhost:8080/job/test-pipeline-job/10/",
                "Status": "FAILURE",
                "Duration": "9 sec",
                "Timestamp": "Fri Jul  3 11:10:41 50815"
            }]
        }

        self.set_context_result = {
            "version": 1.0,
            "current-context": "local-test",
            "contexts": [
                {
                    "context":
                    {
                        "token": "test_token",
                        "url": "test_url",
                        "user": "test_user"
                    },
                    "name": "test"
                },
                {
                    "context":
                    {
                        "token": "local_token",
                        "url": "local_url",
                        "user": "local_user"
                    },
                    "name": "local"
                },
                {
                    "context":
                    {
                        "token": "test-token",
                        "url": "test-url",
                        "user": "test-user"
                    },
                    "name": "local-test"
                }
            ]
        }

        self.set_context_return_1 = {
            "version": 1.0,
            "current-context": "test",
            "contexts": [
                {
                    "context":
                    {
                        "token": "test_token",
                        "url": "test_url",
                        "user": "test_user"
                    },
                    "name": "test"
                },
                {
                    "context":
                    {
                        "token": "test-token",
                        "url": "test-url",
                        "user": "test-user"
                    },
                    "name": "local"
                }
            ]
        }

        self.delete_context_report = {
            "version": 1.0,
            "current-context": "test",
            "contexts": [
                {
                    "context":
                    {
                        "token": "test_token",
                        "url": "test_url",
                        "user": "test_user"
                    },
                    "name": "test"
                }
            ]
        }

        self.delete_current_context_return = {
            "version": 1.0,
            "current-context": "local",
            "contexts": [
                {
                    "context":
                    {
                        "token": "local_token",
                        "url": "local_url",
                        "user": "local_user"
                    },
                    "name": "local"
                }
            ]
        }

        self.rename_context_result = {
            "version": 1.0,
            "current-context": "test",
            "contexts": [
                {
                    "context":
                    {
                        "token": "test_token",
                        "url": "test_url",
                        "user": "test_user"
                    },
                    "name": "test"
                },
                {
                    "context":
                    {
                        "token": "local_token",
                        "url": "local_url",
                        "user": "local_user"
                    },
                    "name": "prod"
                }
            ]
        }

        self.list_context_all = {
            'contexts': [
                {
                    'contextname': 'test*',
                    'contexturl': 'test_url'
                },
                {
                    'contextname': 'local',
                    'contexturl': 'local_url'
                }
            ]
        }

        self.list_context_current = {
            'contexts': [{
                'contextname': 'test*',
                'contexturl': 'test_url'
            }]
        }

        self.list_context_by_name = {
            'contexts': [{
                'contextname': 'local',
                'contexturl': 'local_url'
            }
        ]}

        self.list_context_by_currentname = {
            'contexts': [{
                'contextname': 'test*',
                'contexturl': 'test_url'
            }
        ]}

        self.list_nodes = [
            {
                'name': 'master',
                'offline': False
            }, {
                'name': 'slave1',
                'offline': False
            }
        ]
        self.list_nodes_return = {
            'nodes': [
                {
                    'nodename': 'master',
                    'status': 'Online'
                },{
                    'nodename': 'slave1',
                    'status': 'Online'
                }
            ]
        }

        self.node_info = {
            '_class': 'hudson.slaves.SlaveComputer',
            'actions': [{}],
            'assignedLabels': [
                {'name': 'prod'},
                {'name': 'slave1'},
                {'name': 'test'}
            ], 
            'description': '',
            'displayName': 'slave1',
            'executors': [{}],
            'icon': 'computer.png',
            'iconClassName': 'icon-computer',
            'idle': True, 'jnlpAgent': False,
            'launchSupported': True,
            'loadStatistics': {
                '_class': 'hudson.model.Label$1'
            },
            'manualLaunchAllowed': True,
            'monitorData': {
                'hudson.node_monitors.SwapSpaceMonitor': {
                    '_class': 'hudson.node_monitors.SwapSpaceMonitor$MemoryUsage2',
                    'availablePhysicalMemory': -1,
                    'availableSwapSpace': 878706688,
                    'totalPhysicalMemory': -1,
                    'totalSwapSpace': 1073741824
                },
                'hudson.node_monitors.TemporarySpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/private/var/folders/bw/jshtgwc171dgkvkjc3hrkt1m0000gn/T',
                    'size': 39280267264
                },
                'hudson.node_monitors.DiskSpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/Users/deepan/Documents/Tools/slave1',
                    'size': 39280267264
                },
                'hudson.node_monitors.ArchitectureMonitor': 'Mac OS X (x86_64)',
                'hudson.node_monitors.ResponseTimeMonitor': {
                    '_class': 'hudson.node_monitors.ResponseTimeMonitor$Data',
                    'timestamp': 1559214518883,
                    'average': 195
                },
                'hudson.node_monitors.ClockMonitor': {
                    '_class': 'hudson.util.ClockDifference', 'diff': -65
                }
            },
            'numExecutors': 1,
            'offline': False,
            'offlineCause': None,
            'offlineCauseReason': '',
            'oneOffExecutors': [],
            'temporarilyOffline': False,
            'absoluteRemotePath': '/Users/deepan/Documents/Tools/slave1'
        }

        self.node_info_temp_offline = {
            '_class': 'hudson.slaves.SlaveComputer',
            'actions': [{}],
            'assignedLabels': [
                {'name': 'prod'},
                {'name': 'slave1'},
                {'name': 'test'}
            ], 
            'description': '',
            'displayName': 'slave1',
            'executors': [{}],
            'icon': 'computer.png',
            'iconClassName': 'icon-computer',
            'idle': True, 'jnlpAgent': False,
            'launchSupported': True,
            'loadStatistics': {
                '_class': 'hudson.model.Label$1'
            },
            'manualLaunchAllowed': True,
            'monitorData': {
                'hudson.node_monitors.SwapSpaceMonitor': {
                    '_class': 'hudson.node_monitors.SwapSpaceMonitor$MemoryUsage2',
                    'availablePhysicalMemory': -1,
                    'availableSwapSpace': 878706688,
                    'totalPhysicalMemory': -1,
                    'totalSwapSpace': 1073741824
                },
                'hudson.node_monitors.TemporarySpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/private/var/folders/bw/jshtgwc171dgkvkjc3hrkt1m0000gn/T',
                    'size': 39280267264
                },
                'hudson.node_monitors.DiskSpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/Users/deepan/Documents/Tools/slave1',
                    'size': 39280267264
                },
                'hudson.node_monitors.ArchitectureMonitor': 'Mac OS X (x86_64)',
                'hudson.node_monitors.ResponseTimeMonitor': {
                    '_class': 'hudson.node_monitors.ResponseTimeMonitor$Data',
                    'timestamp': 1559214518883,
                    'average': 195
                },
                'hudson.node_monitors.ClockMonitor': {
                    '_class': 'hudson.util.ClockDifference', 'diff': -65
                }
            },
            'numExecutors': 1,
            'offline': False,
            'offlineCause': None,
            'offlineCauseReason': '',
            'oneOffExecutors': [],
            'temporarilyOffline': True,
            'absoluteRemotePath': '/Users/deepan/Documents/Tools/slave1'
        }

        self.node_info_offline = {
            '_class': 'hudson.slaves.SlaveComputer',
            'actions': [{}],
            'assignedLabels': [
                {'name': 'prod'},
                {'name': 'slave1'},
                {'name': 'test'}
            ], 
            'description': '',
            'displayName': 'slave1',
            'executors': [{}],
            'icon': 'computer.png',
            'iconClassName': 'icon-computer',
            'idle': True, 'jnlpAgent': False,
            'launchSupported': True,
            'loadStatistics': {
                '_class': 'hudson.model.Label$1'
            },
            'manualLaunchAllowed': True,
            'monitorData': {
                'hudson.node_monitors.SwapSpaceMonitor': {
                    '_class': 'hudson.node_monitors.SwapSpaceMonitor$MemoryUsage2',
                    'availablePhysicalMemory': -1,
                    'availableSwapSpace': 878706688,
                    'totalPhysicalMemory': -1,
                    'totalSwapSpace': 1073741824
                },
                'hudson.node_monitors.TemporarySpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/private/var/folders/bw/jshtgwc171dgkvkjc3hrkt1m0000gn/T',
                    'size': 39280267264
                },
                'hudson.node_monitors.DiskSpaceMonitor': {
                    '_class': 'hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace',
                    'timestamp': 1559214518899,
                    'path': '/Users/deepan/Documents/Tools/slave1',
                    'size': 39280267264
                },
                'hudson.node_monitors.ArchitectureMonitor': 'Mac OS X (x86_64)',
                'hudson.node_monitors.ResponseTimeMonitor': {
                    '_class': 'hudson.node_monitors.ResponseTimeMonitor$Data',
                    'timestamp': 1559214518883,
                    'average': 195
                },
                'hudson.node_monitors.ClockMonitor': {
                    '_class': 'hudson.util.ClockDifference', 'diff': -65
                }
            },
            'numExecutors': 1,
            'offline': True,
            'offlineCause': None,
            'offlineCauseReason': '',
            'oneOffExecutors': [],
            'temporarilyOffline': False,
            'absoluteRemotePath': '/Users/deepan/Documents/Tools/slave1'
        }

        self.node_info_return = {
            'slave1': [
                {
                    'Arch': 'Mac OS X (x86_64)',
                    'Executors': 1,
                    'Labels': 'prod, slave1, test',
                    'Name': 'slave1',
                    'Status': 'Online'
                }
            ]
        }

        self.node_info_offline_return = {
            'slave1': [
                {
                    'Name': 'slave1',
                    'Status': 'Disconnected',
                    'Arch': 'Mac OS X (x86_64)',
                    'Labels': 'prod, slave1, test',
                    'Executors': 1,
                    'Reason': ''
                }
            ]
        }
        
        self.node_info_temp_offline_return = {
            'slave1': [
                {
                    'Name': 'slave1',
                    'Status': 'Temporarily Offline',
                    'Arch': 'Mac OS X (x86_64)',
                    'Labels': 'prod, slave1, test',
                    'Executors': 1,
                    'Reason': ''
                }
            ]
        }