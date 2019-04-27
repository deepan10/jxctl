"""
ctxcore - Core context command line methods
"""
import os
import json
import yaml


class CtxCore():
    """
    Command Line Core methods
    Jenkins Context initialization, modification & validation
    """
    CONTEXT_FILE_PATH = "/.jxctl/config"
    USER_HOME = os.path.expanduser('~')
    CONTEXT_FILE = USER_HOME + CONTEXT_FILE_PATH

    @staticmethod
    def init_default_context():
        """
        Initialize the Jenkins default context
        template with NULL values if config not available.
        """
        default_config_file = {
            "current-context": "NULL",
            "context": {
                "url": "NULL",
                "user": "NULL",
                "token": "NULL",
                "name": "NULL",
                }
        }
        user_home = os.path.expanduser('~')
        if not os.path.isdir(user_home+"/.jxctl"):
            os.mkdir(user_home+"/.jxctl")
        config_file = user_home+"/.jxctl/config"
        if not os.path.isfile(config_file):
            with open(config_file, 'w') as yaml_file:
                yaml.dump(yaml.load(
                    json.dumps(default_config_file), Loader=yaml.SafeLoader),
                          yaml_file,
                          default_flow_style=False)

    def get_config_context(self):
        """
        Get context info from config file
        """
        try:
            cfile = open(self.CONTEXT_FILE)
            context = yaml.load(cfile, Loader=yaml.SafeLoader)
            cfile.close()
            return str(context["context"]["user"]), \
                str(context["context"]["token"]), \
                str(context["context"]["url"]), \
                str(context["context"]["name"])
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found Error")

    def __init__(self):
        """
        Init the CtxCore for Command Line context.
        """
        self.init_default_context()
        self.ctx_user, self.ctx_token, self.ctx_url, self.ctx_name = self.get_config_context()  # noqa  # pylint: disable=line-too-long

    def validate_context(self):
        """
        Validate the context to proceed with Jenkins CTL Operations.
        """
        return bool(self.ctx_url and self.ctx_token and self.ctx_user)

    def set_context(self, url, user, token, name):
        """
        Modify the context config
        """
        if user is not None:
            self.ctx_user = user
        if token is not None:
            self.ctx_token = token
        if url is not None:
            self.ctx_url = url
        if name is not None:
            self.ctx_name = name
        context_file = """
            current-context: %s
            context :
                url: %s
                user: %s
                token: %s
                name: %s
            """ % (self.ctx_name,
                   self.ctx_url,
                   self.ctx_user,
                   self.ctx_token,
                   self.ctx_name)
        with open(self.CONTEXT_FILE, 'w') as ctx_file:
            yaml.dump(yaml.load(context_file, Loader=yaml.SafeLoader),
                      ctx_file,
                      default_flow_style=False)
        print("jxctl - context updated")
