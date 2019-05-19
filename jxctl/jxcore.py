"""
jxcore - Core menthods to intract with Jenkins API
"""
import os
import time
import pprint
import jenkins
import requests
from tabulate import tabulate

try:
    from ctxcore import CtxCore
    from jxsupport import JxSupport
except ImportError:
    from .ctxcore import CtxCore
    from .jxsupport import JxSupport


class JxCore():
    """
    jxtl core Jenkins operation methods
    """
    server = ''
    URL = ''
    username = ''
    version = ''
    cwd = ''

    JOB_TYPE = {
        "freestyle": "hudson.model.FreeStyleProject",
        "maven": "hudson.maven.MavenModuleSet",
        "pipeline": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
        "multi-branch": "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject",  # noqa  # pylint: disable=line-too-long
        "folders": "com.cloudbees.hudson.plugins.folder.Folder",
        "matrix": "hudson.matrix.MatrixProject",
        "org": "jenkins.branch.OrganizationFolder"
    }
    NON_JOB_LIST = [
        "com.cloudbees.hudson.plugins.folder.Folder",
        "com.cloudbees.hudson.plugins.modeling.impl.builder.BuilderTemplate",
        "com.cloudbees.hudson.plugins.modeling.impl.jobTemplate.JobTemplate"
    ]

    def __init__(self):
        """
        Initialize the Jenkins Context and CtxCore to access the API
        """
        self.ctx_core = CtxCore()
        self.jxsupport = JxSupport()
        if self.ctx_core.validate_context():
            try:
                self.server = jenkins.Jenkins(self.ctx_core.ctx_url,
                                              username=self.ctx_core.ctx_user,
                                              password=self.ctx_core.ctx_token)
                # pylint: disable=invalid-name
                self.URL = self.ctx_core.ctx_url
                self.cwd = os.getcwd()
            except jenkins.JenkinsException as server_error:
                print("Init Context Core", server_error)
                exit()
        else:
            print("Invalid Jenkins Context ...")
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
            print("Current Context : {0} \n".format(self.ctx_core.ctx_name))
            print(tabulate(info_list,
                           headers=['Type', 'Value'],
                           tablefmt='orgtbl'))
        except requests.exceptions.ConnectionError:
            print("Connection Error... \
                   Make sure your Jenkins context is up and running")

    # @staticmethod
    # def display_table(display_list, display_header, count_flag=False):
    #     """
    #     Display the result in list to Table format.
    #     Having the special param count_flag,
    #     If true will display the count of the list in table.
    #     :param name: OutputList display_list ``list``
    #     :param name: HeaderList display_header ``list``
    #     :param name: Count count_flag ``bool``

    #     Example::
    #         >>> self.display_table(list_item, list_header)
    #         >>> self.display_table(list_item, list_header, count_flag=True)
    #     """
    #     l =[]
    #     for job in display_list.get("plugins"):
    #         l.append([v for k, v in job.items()])
    #     if not count_flag:
    #         print(tabulate(l,
    #                        headers=display_header,
    #                        tablefmt='orgtbl'))
    #     else:
    #         print(tabulate([[len(display_list)]],
    #                        headers=display_header,
    #                        tablefmt='orgtbl'))

    def fetch_job_type(self, search_value):
        """
        Find the key by give the value in DICT
        :param name: Value name search_value ``str``
        :returns: Key of the given Value key ``str``

        Example::
            >>> fetch_job_type(search_value)
        """
        return_key = None
        for key, value in self.JOB_TYPE.items():
            if value == search_value:
                return_key = key
                break
        return return_key

    def list_all_jobs(self, format_display="json", count=False):
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
                if job_item["_class"] not in self.NON_JOB_LIST:
                    jobs_list.extend([{"jobname": job_item["fullname"], "joburl": job_item["url"]}])
            jobs = {"jobs": jobs_list}
        except KeyError:
            raise KeyError("Key not found")
        self.jxsupport.print(jobs, format_display, count)

    def list_jobs(self, option_list, format_display="json", count=False):
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
                    if job_item["_class"] in self.JOB_TYPE[item]:
                        jobs_list.extend([{
                            "jobname": job_item["fullname"],
                            "joburl": job_item["url"]
                        }])
            jobs = {"jobs": jobs_list}
        except KeyError:
            raise KeyError("Key not found")
        self.jxsupport.print(jobs, format_display, count)

    def list_all_plugins(self, format_display="json", count=False):
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
            plugins_list.extend([{"pluginname": item["longName"],
                                  "pluginkey": item["shortName"],
                                  "version": item["version"]}])
        plugins_dict = {"plugins": plugins_list}
        self.jxsupport.print(plugins_dict, format_display, count)

    def get_plugin_info(self, plugin_name):
        """
        Get a plugin info
        """
        pprint.pprint(self.server.get_plugin_info(plugin_name))

    # pylint: disable=unused-argument
    def job_info(self, job_name, format_display="json"):
        """
        Display needed Job info in a table
        :param name: Job name job_name ``str``

        Example::
            >>> job_info(job_name)
        """
        job_json = self.server.get_job_info(job_name)
        job_details = {
            job_json["fullName"]: [{
                "Name": job_json["fullName"],
                "URL": job_json["url"],
                "Type": self.fetch_job_type(job_json["_class"]),
                "Last Completed Build": job_json["lastCompletedBuild"]["number"],
                "Last Sucessful Build": job_json["lastSuccessfulBuild"]["number"],
                "Last Build": job_json["lastBuild"]["number"]
            }]
        }
        self.jxsupport.print(job_details, format_display)

    def build_info(self, job_name, build_no, format_display="json"):
        """
        Build Info
        """
        build_json = self.server.get_build_info(job_name, build_no)
        build_details = {
            job_name: [{
                "Build No.": build_no,
                "URL": build_json["url"],
                "Status": "InProgress" if build_json.get("building") else build_json.get("result"),
                "Duration": "{0} sec".format(int(build_json.get("duration") / 1000)),
                "Timestamp": time.ctime(int(build_json.get("timestamp")))
            }]
        }
        self.jxsupport.print(build_details, format_display)

    def trigger_job(self, job_name, params=None):
        """
        Build a Job
        """
        try:
            self.server.build_job(job_name, params)
            print("jxctl >> \"%s\" triggered sucessfully" % job_name)
        except jenkins.JenkinsException as jenkins_error:
            print(jenkins_error)

    def abort_job(self, job_name, build_number):
        """
        Abort the job build
        """
        self.server.stop_build(job_name, build_number)

    def delete_job(self, job_name):
        """
        Delete a job from Jenkins
        """
        try:
            self.server.delete_job(job_name)
            print("jxctl >> \"%s\" Job deleted" % job_name)
        except jenkins.JenkinsException as jenkins_error:
            print(jenkins_error)

    def list_nodes(self, format_display="json"):
        """
        Get list of nodes
        """
        list_of_nodes = []
        nodes = self.server.get_nodes()
        for node in nodes:
            list_of_nodes.extend([{
                "nodename": node.get("name"),
                "status": "Online" if not node.get("offline") else "Offline"
            }])
        nodes = {"nodes": list_of_nodes}
        self.jxsupport.print(nodes, format_display, False)

    def node_info(self, node_name, format_display="json"):
        """
        Node info
        """
        node_json = self.server.get_node_info(node_name)
        node_details = {
            "Name": node_json["displayName"],
            "Status": "Online",
            "Arch": node_json["monitorData"]["hudson.node_monitors.ArchitectureMonitor"],
            "Labels": ", ".join(
                list(l["name"] for l in node_json["assignedLabels"])
            ),
            "Executors": node_json["numExecutors"]
        }

        if node_json["offline"] and not node_json["temporarilyOffline"]:
            node_details["Status"] = "Disconnected"
            node_details["Reason"] = node_json.get("offlineCauseReason")

        if node_json["temporarilyOffline"]:
            node_details["Status"] = "Temporarily Offline"
            node_details["Reason"] = node_json.get("offlineCauseReason")

        node = {
            node_name: [node_details]
        }
        self.jxsupport.print(node, format_display)

    def node_action(self, node_name, action, message=None):
        """
        Node operations like make offile and online
        """
        if action == "offline":
            self.server.disable_node(node_name, msg=message)
        elif action == "online":
            self.server.enable_node(node_name)
