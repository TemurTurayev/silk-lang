"""
Tests for dict .toCodeDeploy3Config() method - format as CodeDeploy v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCodeDeploy3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeDeploy3Config_basic(self):
        output = self._run('print({"application": "my-app"}.toCodeDeploy3Config())')
        assert output[-1] == "application = my-app"

    def test_toCodeDeploy3Config_multi(self):
        output = self._run('print({"application": "my-app", "group": "prod"}.toCodeDeploy3Config())')
        assert output[-1] == "application = my-app\ngroup = prod"
