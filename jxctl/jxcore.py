import os
import sys
import yaml
import jenkins
import json
import time
from tabulate import tabulate
from json2html import json2html
#from json2html import *

#sys.path.append("..")

try:
    from ctlcore import ctlCore
except ImportError:
    from .ctlcore import ctlCore

class pyjenkins:
   
    server = ''
    URL = ''
    username = ''    
    version = ''
    cwd = ''

    option_dist = {
        "freestyle" : "hudson.model.FreeStyleProject", 
        "maven" : "hudson.maven.MavenModuleSet", 
        "pipeline" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
        "multi-branch" : "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject",
        "folders" : "com.cloudbees.hudson.plugins.folder.Folder",
        "matrix" : "hudson.matrix.MatrixProject",
        "org" : "jenkins.branch.OrganizationFolder"
    }
    non_jobs_list = [ 
        "com.cloudbees.hudson.plugins.folder.Folder",
        "com.cloudbees.hudson.plugins.modeling.impl.builder.BuilderTemplate",
        "com.cloudbees.hudson.plugins.modeling.impl.jobTemplate.JobTemplate"
	]

    build_info_dict = {
        "_class" : "Style",
        "shortDescription" : "Started By",
        "url" : "Job URL",
        "remoteUrls" : "SCM URL",
        "commitId" : "Commit ID",
        "fullDisplayName" : "Display Name",
        "result" : "Status",
        "timestamp" : "Time"
    }

    BUILD_DETAILS = {
        "Job Type" : "_class",
        "Started By" : ["actions", "shortDescription"],
        "URL" : "url",
        "Commit Id" : ['actions', "SHA1"],
        "Job Name" : ['actions', "name"],
        "SCM URL" : ["actions","remoteUrls"],
        "Comment" : ["changeSets", "comment"],
        "Name" : "fullDisplayName",
        "Build Status" : "result",
        "Time" : "timestamp"
    }

    JOB_DETAILS = {
        "Name" : "fullName",
        "URL" : "url",
        "Type" : "_class",
        "Last Completed Build" : ["lastCompletedBuild","number"],
        "Last Sucessful Build" : ["lastSuccessfulBuild","number"],
        "Last Build" : ["lastBuild","number"],
        "SCM Type" : ["scm", "_class"],
        "Builds" : ["builds", "number"]
    }

    def __init__(self):
        ctl = ctlCore()
        if ctl.validate_context():
            try:
                self.server = jenkins.Jenkins(ctl.cURL, username=ctl.cUser, password=ctl.cToken)
                self.URL = ctl.cURL     
                self.cwd = os.getcwd()           
            except Exception as e:
                print(e)
                exit()
        else:
            print("Please validate the Jenkins Context before proceeding...")
            exit()
    
    def info(self):
        self.username = self.server.get_whoami()["fullName"]
        self.version = self.server.get_version()
        info_list = [["URL", self.URL], ["Version", self.version], ["User", self.username]]
        print(tabulate(info_list, headers=['Jenkins', 'Description'], tablefmt='orgtbl'))       

    def displayTable(self, displayList = [], displayHeader = [], countFlag = False):
        if not countFlag:
            print(tabulate(displayList, headers=displayHeader, tablefmt='orgtbl'))  
        else:
            print(tabulate([[len(displayList)]], headers=displayHeader, tablefmt='orgtbl'))

    def json2list(self, json):
        return [(key,value) for key,value in json.items()]
    
    def key_from_value(self, job_class):
        for key,value in self.option_dist.items():
            if value == job_class:
                return key
    
    def get_json_info(self, node, kv):
        if isinstance(node, list):
            for i in node:
                for x in self.get_json_info(i, kv):                
                    yield x
        elif isinstance(node, dict):
            if kv in node:
                yield node[kv]
            for j in node.values():
                for x in self.get_json_info(j, kv):
                    yield x  
    
    def detailsFromJSON(self, srcJSON, searchJSON, jobflag):
        info_list = []
        for name, item in searchJSON.items():
            if type(item) is list:                
                if len(list(self.get_json_info(srcJSON, item[0]))) != 0: 
                    if jobflag:                   
                        info_list.append([name, list(self.get_json_info(srcJSON[item[0]], item[1]))])                    
                    else:
                        info_list.append([name, list(self.get_json_info(srcJSON[item[0]], item[1]))[0]]) 
            else:
                if len(list(self.get_json_info(srcJSON, item))) != 0:
                    info_list.append([name, srcJSON[item]])
        return info_list

##################################################################################################################################

    # jxcore - Job functions
    def _list_all_jobs(self):
        jobs_list = []
        try:
            jobs = self.server.get_all_jobs(folder_depth=None, folder_depth_per_request=50)
            for job_item in jobs:
                if(job_item["_class"] not in self.non_jobs_list):
                    jobs_list.append([job_item["fullname"], job_item["url"]])
        except ValueError as ve:
            print("Json Error", ve)
        return jobs_list

    def list_all_jobs(self, count = False):
        jobs_list = self._list_all_jobs()
        if not count:
            self.displayTable(jobs_list, ['Name', 'URL'])
        else:
            self.displayTable(jobs_list, ['No. of Jobs'], countFlag=True)    
    
    def _list_jobs(self, option_list):
        jobs_list = []
        jobs = self.server.get_all_jobs(folder_depth=None, folder_depth_per_request=50)
        for item in option_list:
            for job_item in jobs:                        
                if(job_item["_class"] in self.option_dist[item]):
                    jobs_list.append([job_item["fullname"], job_item["url"]])
        return jobs_list

    def list_jobs(self, option_list, count=False):
        jobs_list = self._list_jobs(option_list)
        if not count:
            self.displayTable(jobs_list, ['Name', 'URL'])
        else:
            self.displayTable(jobs_list, ['No. of Jobs'], countFlag=True)
    
    # jxcore - Plugin functions
    def _list_all_plugins(self):
        plugins = self.server.get_plugins_info()
        plugins_list = []
        for item in plugins:
            plugins_list.append([item["longName"], item["shortName"], item["version"]])
        return plugins_list

    def list_all_plugins(self, count=False):
        plugins_list = self._list_all_plugins()
        if not count:
            self.displayTable(plugins_list, ['Plugin Name', 'Short Name', 'Version'])
        else:
            self.displayTable(plugins_list, ['No. of Plugins'], True)

    # jxcore - genrate report
    def genrate_report(self, report, json):
        f = open("report.html", "w")
        if json:
            html_report = json2html.convert(json = report)
            f.write(html_report)
            f.close()
            print("Detail Job Report \"%s/report.html\" generated sucessfully" % self.cwd)
        else:
            html_report = tabulate(report, headers=['Job', 'Details'], tablefmt='orgtbl')
            f.write(html_report)
            f.close()
            print("Detail Job Report \"%s/report.html\" generated sucessfully" % self.cwd)
        
    # jxcore - job info
    def _job_info(self, jobName):
        job_json = self.server.get_job_info(jobName)  
        job_info_list = self.detailsFromJSON(job_json, self.JOB_DETAILS, jobflag=True)
        return job_info_list

    def job_info(self, jobName, debug=False, report=False):
        self.displayTable(self._job_info(jobName), ["Job Data","Detail"])                   

    def build_info(self, jobName, buildNumber):
        build_json = self.server.get_build_info(jobName, buildNumber)
        #build_info_list = []
        #for name, item in self.BUILD_DETAILS.items():       
            #if type(item) is list:                
                #if len(list(self.get_json_info(build_json, item[0]))) != 0:                    
                    #build_info_list.append([name, list(self.get_json_info(build_json[item[0]], item[1]))[0]])                    
            #else:
                #if len(list(self.get_json_info(build_json, item))) != 0:
                    #build_info_list.append([name, build_json[item]])
        self.displayTable(self.detailsFromJSON(build_json, self.BUILD_DETAILS, jobflag=False),["Build Data","Detail"])
    
    def job_build(self, jobName):
        self.server.build_job(jobName)
        print("jxctl >> \"%s\" triggered sucessfully" % jobName)