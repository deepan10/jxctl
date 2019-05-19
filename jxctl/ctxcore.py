"""
ctxcore - Core context command line methods
"""
import os
import json
import yaml

try:
    from jxsupport import JxSupport
except ImportError:
    from .jxsupport import JxSupport


class CtxCore():
    """
    Command Line Core methods
    Jenkins Context initialization, modification & validation
    """
    USER_HOME = os.path.expanduser('~')
    CONTEXT_FILE_PATH = USER_HOME + "/.jxctl"
    CONTEXT_FILE = CONTEXT_FILE_PATH + "/config"
    jx_context = None
    DEFAULT_CONTEXT = {
        'version': 1.0,
        'current-context': 'default',
        'contexts': [
            {
                'context':
                {
                    'token': None,
                    'url': None,
                    'user': None
                },
                'name': 'default'
            }
        ]
    }

    def __init__(self):
        """
        Init the CtxCore for Command Line context.
        """
        self.jxsupport = JxSupport()
        self.ctx_url = self.ctx_name = self.ctx_user = self.ctx_token = None
        self.context_list = []

        self._set_default_context_file()
        self.load_context()

    def _set_default_context_file(self):
        """
        Initialize the Jenkins default context
        template with NULL values if config not available.
        """
        if not os.path.isdir(self.CONTEXT_FILE_PATH):
            os.mkdir(self.CONTEXT_FILE_PATH)
        if not os.path.isfile(self.CONTEXT_FILE):
            with open(self.CONTEXT_FILE, 'w') as yaml_file:
                yaml.dump(yaml.load(json.dumps(self.DEFAULT_CONTEXT),
                                    Loader=yaml.SafeLoader),
                          yaml_file,
                          default_flow_style=False)

    def load_context(self):
        """
        Load context file
        """
        try:
            with open(self.CONTEXT_FILE, "r") as context_file:
                self.jx_context = yaml.load(context_file, Loader=yaml.SafeLoader)
        except FileNotFoundError:
            raise FileNotFoundError("File {0} not found".format(self.CONTEXT_FILE))

        for context in self.jx_context["contexts"]:
            self.context_list.append(context["name"])
            if context["name"] == self.jx_context["current-context"]:
                self.ctx_url = context["context"]["url"]
                self.ctx_user = context["context"]["user"]
                self.ctx_token = context["context"]["token"]
                self.ctx_name = context["name"]

    def write_context_file(self):
        """
        Write changes to context config file
        """
        with open(self.CONTEXT_FILE, 'w') as yaml_file:
            yaml.dump(
                yaml.load(
                    json.dumps(self.jx_context),
                    Loader=yaml.SafeLoader
                ),
                yaml_file,
                default_flow_style=False
            )

    def set_current_context(self, name):
        """
        Change the current context
        """
        if name in self.context_list:
            self.jx_context["current-context"] = name
            self.write_context_file()
        else:
            print("Not a valid context..")

    # pylint:  disable=too-many-arguments
    def set_context(self, name, url=None, user=None, token=None, default=None):
        """
        Add/Edit Jenkins context
        """
        if name in self.context_list:
            for context in self.jx_context["contexts"]:
                if context["name"] == name:
                    context["context"]["url"] = url if url else context["context"]["url"]
                    context["context"]["user"] = user if user else context["context"]["user"]
                    context["context"]["token"] = token if token else context["context"]["token"]
        else:
            new_context = {
                'context': {
                    'token': token,
                    'url': url,
                    'user': user
                },
                'name': name
            }
            self.jx_context["contexts"].append(new_context)
        if default:
            self.jx_context["current-context"] = name
        self.write_context_file()

    # pylint: disable=redefined-builtin
    def list_context(self, all=None, context_name=None):
        """
        List Jenkins context
        """
        context_list = []
        if all:
            for context in self.jx_context["contexts"]:
                if context.get("name") == self.jx_context.get("current-context"):
                    context_list.extend([
                        {
                            "contextname": context["name"] + "*",
                            "contexturl": context["context"]["url"]
                        }
                    ])
                else:
                    context_list.extend([
                        {
                            "contextname": context["name"],
                            "contexturl": context["context"]["url"]
                        }
                    ])
        elif context_name:
            for context in self.jx_context.get("contexts"):
                if context.get("name") == context_name:
                    if context.get("name") == self.jx_context.get("current-context"):
                        context_list.extend([
                            {
                                "contextname": context["name"] + "*",
                                "contexturl": context["context"]["url"]
                            }
                        ])
                    else:
                        context_list.extend([
                            {
                                "contextname": context["name"],
                                "contexturl": context["context"]["url"]
                            }
                        ])
        else:
            for context in self.jx_context.get("contexts"):
                if context.get("name") == self.jx_context.get("current-context"):
                    context_list.extend([
                        {
                            "contextname": context["name"] + "*",
                            "contexturl": context["context"]["url"]
                        }
                    ])

        context_dict = {"contexts": context_list}
        self.jxsupport.print(context_dict, "table", count=False)

    def delete_context(self, context_name):
        """
        Delete the context
        """
        import pprint
        pprint.pprint(self.jx_context)
        if self.jx_context["current-context"] == context_name:
            self.jx_context["current-context"] = self.jx_context["contexts"][0]["name"]

        for context in self.jx_context["contexts"]:
            if context["name"] == context_name:
                self.jx_context["contexts"].remove(context)
        self.write_context_file()

    def rename_context(self, context_from, context_to):
        """
        Rename the context name
        """
        if context_from in self.context_list:
            for context in self.jx_context["contexts"]:
                if context["name"] == context_from:
                    context["name"] = context_to
            self.write_context_file()

    def validate_context(self):
        """
        Validate the context to proceed with Jenkins CTL Operations.
        """
        return bool(self.ctx_url and self.ctx_token and self.ctx_user)
