"""
Tests for dict .toAppConfig2Config() method - format as AppConfig config.
"""

from silk.interpreter import Interpreter


class TestDictToAppConfig2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppConfig2Config_basic(self):
        output = self._run('print({"appId": "my-app"}.toAppConfig2Config())')
        assert output[-1] == "appId = my-app"

    def test_toAppConfig2Config_multi(self):
        output = self._run('print({"appId": "my-app", "envId": "prod"}.toAppConfig2Config())')
        assert "appId = my-app" in output[-1]
