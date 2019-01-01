from .test_base import jxctlTestBase

class jxCoreTest(jxctlTestBase):
    def test_json2list(self):
        json_object={
            '_class': 'FreeStyle',
            'name': 'test'
        }
        return_value = [['_class', 'FreeStyle'], ['name', 'test']]
        self.assertCountEqual(self.jxctl_context.json2list(json_object),return_value)
