import json
from mock import patch
import jenkins

import sys
sys.path.append("..")

from .test_base import jxctlTestBase

class JenkinsListPlugins(jxctlTestBase):
    all_plugins = []
    @patch.object(jenkins.Jenkins, 'get_plugins_info')
    def test_list_plugins(self, mock_plugins):
        self.maxDiff = None
        mock_plugins.return_value = self.plugins_list
        self.all_plugins = self.jxctl_context._list_all_plugins()
        self.assertListEqual(self.all_plugins, self.plugins_list_return)