
import unittest
from unittest import mock
from mock import patch, mock_open

from jxctl.ctxcore import CtxCore

class TestCtxCore(unittest.TestCase):
    
    @mock.patch('jxctl.ctxcore.CtxCore.get_config_context')
    @mock.patch('jxctl.ctxcore.CtxCore.init_default_context')
    def test_validate_context(self, mock_default_context, mock_config_context):
        mock_config_context.return_value = "ctx_user", "ctx_token", "ctx_url", "ctx_name"
        ctx_obj = CtxCore()
        result = ctx_obj.validate_context()
        mock_default_context.assert_called_once()
        self.assertEqual(result, True)

    @mock.patch('jxctl.ctxcore.CtxCore.init_default_context')
    @mock.patch('yaml.load')
    def test_get_config_context(self, mock_yaml, mock_default_context):
        context = {'context': {'name': 'localhost', 'token': 'admin', 'url': 'http://localhost:8080', 'user': 'admin'}, 'current-context': 'localhost'}
        
        mock_yaml.return_value = context
        with patch("builtins.open", mock_open()):
            ctx_obj = CtxCore()
        self.assertEqual(ctx_obj.ctx_user, context['context']['user'])
        self.assertEqual(ctx_obj.ctx_token, context['context']['token'])
        self.assertEqual(ctx_obj.ctx_url, context['context']['url'])
        self.assertEqual(ctx_obj.ctx_name, context['context']['name'])
        mock_default_context.assert_called_once()
    
    @mock.patch('jxctl.ctxcore.CtxCore.init_default_context')
    def test_get_config_context_invalid_file(self, mock_default_context):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError()
            with self.assertRaises(FileNotFoundError) as context_manager:
                CtxCore()
            self.assertEqual(str(context_manager.exception), "File Not Found Error")
        mock_default_context.assert_called_once()
    
    @mock.patch('jxctl.ctxcore.CtxCore.get_config_context')
    @mock.patch('jxctl.ctxcore.CtxCore.init_default_context')
    @mock.patch('yaml.dump')
    def test_set_context(self, mock_yaml, mock_default_context, mock_config_context):
        mock_config_context.return_value = "ctx_user", "ctx_token", "ctx_url", "ctx_name"
        with patch("builtins.open", mock_open()):
            ctx_obj = CtxCore()
            ctx_obj.set_context("url", "user", "token", "name")
        mock_default_context.assert_called_once()
        mock_yaml.assert_called_once()

    @mock.patch('os.path.isfile')
    @mock.patch('os.path.isdir')
    @mock.patch('os.mkdir')
    @mock.patch('jxctl.ctxcore.CtxCore.get_config_context')
    def test_init_default_context(self, mock_config_context, mock_mkdir, mock_os_path, mock_os_file):
        mock_os_file.return_value = False
        mock_os_path.return_value = False
        mock_config_context.return_value = "ctx_user", "ctx_token", "ctx_url", "ctx_name"
        with patch("builtins.open", mock_open()):
            CtxCore()
        mock_mkdir.assert_called_once()
