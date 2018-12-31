import json
import mock
from mock import patch
import jenkins


import sys
sys.path.append("..")

import unittest
from jxctl.jxcore import PyJenkins
from jxctl.ctxcore import CtxCore
from .test_jsons import TestCasesInput

class jxctlTestBase(unittest.TestCase):

    @patch.object(CtxCore, 'validate_context')
    def init_pyjenkins(self, mocl_context=False):
        mocl_context.return_value = True
        self.jxctl_context = PyJenkins()
    
    def setUp(self):
        super(jxctlTestBase, self).setUp()
        self.init_pyjenkins()
        #self.load_JSONS()
        self.jsons = TestCasesInput()

    def tearDown(self):
        pass

