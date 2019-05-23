"""
Test ctxcore.py
"""
import unittest
from unittest import mock
from mock import patch, mock_open

from jxctl.ctxcore import CtxCore
from .support_json import SupportJSON

class TestCtxCore(unittest.TestCase):

    def setUp(self):
        self.TEST_CONTEXT = """
        {
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
                    "name": "local"
                }
            ]
        }
        """

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_current_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_current_context("local")
        self.assertEqual(ctx_obj.jx_context["current-context"], "local")
        mock_write.assert_called_once()

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_context("local-test", "test-url", "test-user", "test-token")
        self.assertEqual(ctx_obj.jx_context, SupportJSON().set_context_result)
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_list_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.list_context()
        #Need to implement the print assert equal

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_delete_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.delete_context("local")
        self.assertEqual(ctx_obj.jx_context, SupportJSON().delete_context_report)
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_rename_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.rename_context("local", "prod")
        self.assertEqual(ctx_obj.jx_context, SupportJSON().rename_context_result)
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    def test_validate_context(self, mock_default_context):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            result = ctx_obj.validate_context()
        mock_default_context.assert_called_once()
        self.assertEqual(result, True)