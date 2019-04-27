import json
import mock
from mock import patch
import jenkins


import sys
sys.path.append("..")

import unittest
from jxctl.jxcore import JxCore
from jxctl.ctxcore import CtxCore
from .support_json import SupportJSON

class jxctlTestBase(unittest.TestCase):

    @patch.object(CtxCore, 'validate_context')
    def init_pyjenkins(self, mock_context=False):
        mock_context.return_value = True
        self.jxctl_context = JxCore()
    
    def setUp(self):
        super(jxctlTestBase, self).setUp()
        self.init_pyjenkins()
        #self.load_JSONS()
        self.jsons = SupportJSON()

    def tearDown(self):
        pass

