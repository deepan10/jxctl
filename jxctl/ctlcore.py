import os
import yaml
import json

class ctlCore:
    CONTEXT_FILE_PATH = "/.jxctl/config"
    USER_HOME = os.path.expanduser('~')
    CONTEXT_FILE = USER_HOME + CONTEXT_FILE_PATH

    cUser = cToken = cURL = cName = ''

    def init_jxctl_context(self):
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
                yaml.dump(yaml.load(json.dumps(default_config_file)), yaml_file, default_flow_style=False)



    def __init__(self):
        self.init_jxctl_context()

        cfile = open(self.CONTEXT_FILE)
        context = yaml.load(cfile)
        self.cUser = str(context["context"]["user"])
        self.cToken = str(context["context"]["token"])
        self.cURL = str(context["context"]["url"])
        self.cName = str(context["context"]["name"])
        cfile.close()
        #self.validate_context()
        #print(self.cName, self.cToken, self.cURL, self.cUser)

    def validate_context(self):
        if (self.cURL != "NULL") and (self.cToken != "NULL") and (self.cUser != "NULL"):
            return True
        else:
            return False

    def set_context(self, url, user, token, name):
        if user is not None:
            self.cUser = user
        if token is not None:
            self.cToken = token
        if url is not None:
            self.cURL = url

        if name is not None:
            self.cName = name        

        context_file = """
            current-context: %s
            context :
                url: %s
                user: %s
                token: %s
                name: %s
            """ % (self.cName, self.cURL, self.cUser, self.cToken, self.cName)
        #print(yaml.dump(yaml.load(context_file), default_flow_style=False))

        with open(self.CONTEXT_FILE, 'w') as cFile:
            yaml.dump(yaml.load(context_file), cFile, default_flow_style=False)

        print("jxctl - context updated")
        
