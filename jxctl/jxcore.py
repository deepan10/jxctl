"""
jxcore - Core menthods to intract with Jenkins API
"""
import os
import jenkins
import requests
from tabulate import tabulate
from json2html import json2html

try:
    from ctxcore import CtxCore
except ImportError:
    from .ctxcore import CtxCore


class JxCore():
    """
    jxtl core Jenkins operation methods
    """
    server = ''
    URL = ''
    username = ''
    version = ''
    cwd = ''

    option_dist = {
        "freestyle": "hudson.model.FreeStyleProject",
        "maven": "hudson.maven.MavenModuleSet",
        "pipeline": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
        "multi-branch": "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject",  # noqa  # pylint: disable=line-too-long
        "folders": "com.cloudbees.hudson.plugins.folder.Folder",
        "matrix": "hudson.matrix.MatrixProject",
        "org": "jenkins.branch.OrganizationFolder"
    }
    non_jobs_list = [
        "com.cloudbees.hudson.plugins.folder.Folder",
        "com.cloudbees.hudson.plugins.modeling.impl.builder.BuilderTemplate",
        "com.cloudbees.hudson.plugins.modeling.impl.jobTemplate.JobTemplate"
        ]

    build_info_dict = {
        "_class": "Style",
        "shortDescription": "Started By",
        "url": "Job URL",
        "remoteUrls": "SCM URL",
        "commitId": "Commit ID",
        "fullDisplayName": "Display Name",
        "result": "Status",
        "timestamp": "Time"
    }

    BUILD_DETAILS = {
        "Job Type": "_class",
        "Started By": ["actions", "shortDescription"],
        "URL": "url",
        "Commit Id": ['actions', "SHA1"],
        "Job Name": ['actions', "name"],
        "SCM URL": ["actions", "remoteUrls"],
        "Comment": ["changeSets", "comment"],
        "Name": "fullDisplayName",
        "Build Status": "result",
        "Time": "timestamp"
    }

    JOB_DETAILS = {
        "Name": "fullName",
        "URL": "url",
        "Type": "_class",
        "Last Completed Build": ["lastCompletedBuild", "number"],
        "Last Sucessful Build": ["lastSuccessfulBuild", "number"],
        "Last Build": ["lastBuild", "number"],
        "SCM Type": ["scm", "_class"],
        "Builds": ["builds", "number"]
    }

    def __init__(self):
        """
        Initialize the Jenkins Context and CtxCore to access the API
        """
        ctx_core = CtxCore()
        if ctx_core.validate_context():
            try:
                self.server = jenkins.Jenkins(ctx_core.ctx_url,
                                              username=ctx_core.ctx_user,
                                              password=ctx_core.ctx_token)
                # pylint: disable=invalid-name
                self.URL = ctx_core.ctx_url
                self.cwd = os.getcwd()
            except jenkins.JenkinsException as server_error:
                print("Init Context Core", server_error)
                exit()
        else:
            print("Please validate the Jenkins Context before proceeding...")
            exit()

    def info(self):
        """
        Display the Context Information

        Example::
            >>> jxctl context info
        """
        try:
            self.username = self.server.get_whoami()["fullName"]
            self.version = self.server.get_version()
            info_list = [
                ["URL", self.URL],
                ["Version", self.version],
                ["User", self.username]]
            print(tabulate(info_list,
                           headers=['Jenkins', 'Description'],
                           tablefmt='orgtbl'))
        except requests.exceptions.ConnectionError:
            print("Connection Error... \
                   Make sure your Jenkins context is up and running")

    @staticmethod
    def display_table(display_list, display_header, count_flag=False):
        """
        Display the result in list to Table format.
        Having the special param count_flag,
        If true will display the count of the list in table.
        :param name: OutputList display_list ``list``
        :param name: HeaderList display_header ``list``
        :param name: Count count_flag ``bool``

        Example::
            >>> self.display_table(list_item, list_header)
            >>> self.display_table(list_item, list_header, count_flag=True)
        """
        if not count_flag:
            print(tabulate(display_list,
                           headers=display_header,
                           tablefmt='orgtbl'))
        else:
            print(tabulate([[len(display_list)]],
                           headers=display_header,
                           tablefmt='orgtbl'))

    def key_from_value(self, search_value):
        """
        Find the key by give the value in DICT
        :param name: Value name search_value ``str``
        :returns: Key of the given Value key ``str``

        Example::
            >>> key_from_value(search_value)
        """
        return_key = None
        for key, value in self.option_dist.items():
            if value == search_value:
                return_key = key
                break
        return return_key

    def search_json(self, node, src_json):
        """
        Search key, value from JSON
        :param name: Source JSON node ``dist``
        :param name: Search string src_json ``str``
        :returns: JSON ``dist``

        Example::
            >>> search_json(node, src_json)
        """
        if isinstance(node, list):
            for node_value in node:
                for value in self.search_json(node_value, src_json):
                    yield value
        elif isinstance(node, dict):
            if src_json in node:
                yield node[src_json]
            for node_value in node.values():
                for value in self.search_json(node_value, src_json):
                    yield value

    def details_from_json(self,
                          src_json,
                          search_json,
                          jobflag):
        """
        Returns Details from JSON by giving source DICT
        & search DICT (items needs to be fetched) as a list
        :param name: Source JSON src_json ``dict``
        :param name: Search JSON search_json ``dict``
        :param name: Determine source DICT is JOB / Build ``bool``
        :returns: INFO list info_list ``list``

        Example::
            >>> details_from_json(src_json, search_json, true):
        """
        info_list = []
        for name, item in search_json.items():
            if isinstance(item, (list)):
                if list(self.search_json(src_json, item[0])):
                    if jobflag:
                        info_list.append([name,
                                          list(self.search_json(
                                              src_json[item[0]],
                                              item[1])
                                              )])
                    else:
                        search_list = list(self.search_json(src_json[item[0]],
                                                            item[1]))
                        if search_list:
                            info_list.append([name, search_list[0]])
            else:
                if list(self.search_json(src_json, item)):
                    info_list.append([name, src_json[item]])
        return info_list

    def list_all_jobs(self, count=False):
        """
        Display all jobs in Jenkins Context in a table
        :param name: Count count ``bool``

        Example::
            >>> list_all_jobs()
            >>> list_all_jobs(count=True)
        """
        jobs_list = []
        jobs = self.server.get_all_jobs(folder_depth=None,
                                        folder_depth_per_request=50)
        try:
            for job_item in jobs:
                if job_item["_class"] not in self.non_jobs_list:
                    jobs_list.append([job_item["fullname"], job_item["url"]])
        except KeyError:
            raise KeyError("Key not found")

        if not count:
            self.display_table(jobs_list, ['Name', 'URL'])
        else:
            self.display_table(jobs_list, ['No. of Jobs'], count_flag=True)

    def list_jobs(self, option_list, count=False):
        """
        Display only the specified class jobs in a table
        :param name: Job class list option_list ``list``
        :param name: Count count ``bool``

        Example::
            >>> list_jobs(option_list)
            >>> list_jobs(option_list, count=True)
        """
        jobs_list = []
        jobs = self.server.get_all_jobs(folder_depth=None,
                                        folder_depth_per_request=50)
        try:
            for item in option_list:
                for job_item in jobs:
                    if job_item["_class"] in self.option_dist[item]:
                        jobs_list.append([job_item["fullname"],
                                          job_item["url"]])
        except KeyError:
            raise KeyError("Key not found")

        if not count:
            self.display_table(jobs_list, ['Name', 'URL'])
        else:
            self.display_table(jobs_list, ['No. of Jobs'], count_flag=True)

    def list_all_plugins(self, count=False):
        """
        Display all plugins in Jenkins context as a table
        :param name: count flag count ``bool``

        Example::
            >>> list_all_plugins()
            >>> list_all_plugins(count=True)
        """
        plugins = self.server.get_plugins_info()
        plugins_list = []
        for item in plugins:
            plugins_list.append([item["longName"],
                                 item["shortName"],
                                 item["version"]])

        if not count:
            self.display_table(plugins_list,
                               ['Plugin Name', 'Short Name', 'Version'])
        else:
            self.display_table(plugins_list, ['No. of Plugins'], True)

    # jxcore - genrate report
    def genrate_report(self, report, json):
        """
        Generate HTML Report
        """
        report_file = open("report.html", "w")
        if json:
            html_report = json2html.convert(json=report)
            report_file.write(html_report)
            report_file.close()
            print("Detail Job Report \"%s \
                  /report.html\" generated \
                  sucessfully" % self.cwd)
        else:
            html_report = tabulate(report,
                                   headers=['Job', 'Details'],
                                   tablefmt='orgtbl')
            report_file.write(html_report)
            report_file.close()
            print("Detail Job Report \"%s \
                  /report.html\" generated \
                  sucessfully" % self.cwd)

    # pylint: disable=unused-argument
    def job_info(self, job_name, debug=False, report=False):
        """
        Display needed Job info in a table
        :param name: Job name job_name ``str``
        :param name: Detailed Info debug ``bool``
        :param name: Reported to a file report ``bool``

        Example::
            >>> job_info(job_name)
        """
        job_json = self.server.get_job_info(job_name)
        job_info_list = self.details_from_json(job_json,
                                               self.JOB_DETAILS,
                                               jobflag=True)
        self.display_table(job_info_list, ["Job Data", "Detail"])

    def build_info(self, job_name, build_no):
        """
        Build Info
        """
        build_json = self.server.get_build_info(job_name, build_no)
        build_info_list = self.details_from_json(build_json,
                                                 self.BUILD_DETAILS,
                                                 jobflag=False)
        self.display_table(build_info_list, ["Build Data", "Detail"])

    def job_build(self, job_name):
        """
        Build a Job
        """
        self.server.build_job(job_name)
        print("jxctl >> \"%s\" triggered sucessfully" % job_name)
