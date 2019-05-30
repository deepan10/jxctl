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
    def test_load_context(self, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
        self.assertEqual("test", ctx_obj.ctx_name)
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("builtins.open")
    def test_load_context_raise_error(self, mock_open, _):
        mock_open.side_effect = FileNotFoundError()
        with self.assertRaises(FileNotFoundError) as exception:
            ctx_obj = CtxCore()
            self.assertEqual(exception.exception, FileNotFoundError(ctx_obj.CONTEXT_FILE))

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("yaml.load")
    def test_load_context_raise_typeerror(self, mock_yaml, _):
        mock_yaml.side_effect = TypeError()
        with patch("builtins.open", mock_open(read_data="")):
            with self.assertRaises(TypeError) as exception:
                ctx_obj = CtxCore()
                self.assertEqual(exception.exception, TypeError())

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_current_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_current_context("local")
        self.assertEqual(ctx_obj.jx_context["current-context"], "local")
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.print")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_current_context_invalid(self, mock_write, mock_print, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_current_context("local-dev")
        mock_print.assert_called_with("Not a valid context..")

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_context_new(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_context("local-test", "test-url", "test-user", "test-token", True)
        self.assertEqual(ctx_obj.jx_context, SupportJSON().set_context_result)
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    def test_set_context(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.set_context("local", "test-url", "test-user", "test-token")
        self.assertEqual(ctx_obj.jx_context, SupportJSON().set_context_return_1)
        mock_write.assert_called_once()
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    def test_list_context_all(self, mock_print, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.list_context(all=True)
        mock_print.assert_called_with(SupportJSON().list_context_all, "table", count=False)

    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    def test_list_context_current(self, mock_print, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.list_context()
        mock_print.assert_called_with(SupportJSON().list_context_current, "table", count=False)
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    def test_list_context_name(self, mock_print, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.list_context(context_name="local")
        mock_print.assert_called_with(SupportJSON().list_context_by_name, "table", count=False)
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    @mock.patch("jxctl.ctxcore.CtxCore.write_context_file")
    @mock.patch("jxctl.jxsupport.JxSupport.print")
    def test_list_context_currentname(self, mock_print, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.list_context(context_name="test")
        mock_print.assert_called_with(SupportJSON().list_context_by_currentname, "table", count=False)

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
    def test_delete_currentcontext(self, mock_write, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.delete_context("test")
        self.assertEqual(ctx_obj.jx_context, SupportJSON().delete_current_context_return)
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
    @mock.patch("jxctl.ctxcore.print")
    def test_rename_context_invalid(self, mock_print, _):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            ctx_obj.rename_context("local-dev", "local")
        mock_print.assert_called_with("Not a valid context..")
    
    @mock.patch("jxctl.ctxcore.CtxCore._set_default_context_file")
    def test_validate_context(self, mock_default_context):
        with patch("builtins.open", mock_open(read_data=self.TEST_CONTEXT)):
            ctx_obj = CtxCore()
            result = ctx_obj.validate_context()
        mock_default_context.assert_called_once()
        self.assertEqual(result, True)