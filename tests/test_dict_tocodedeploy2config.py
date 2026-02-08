"""
Tests for dict .toCodeDeploy2Config() method - format as CodeDeploy config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeDeploy2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeDeploy2Config_basic(self):
        output = self._run('print({"applicationName": "my-app"}.toCodeDeploy2Config())')
        assert output[-1] == "applicationName = my-app"

    def test_toCodeDeploy2Config_multi(self):
        output = self._run('print({"applicationName": "my-app", "deploymentGroup": "prod"}.toCodeDeploy2Config())')
        assert "applicationName = my-app" in output[-1]
