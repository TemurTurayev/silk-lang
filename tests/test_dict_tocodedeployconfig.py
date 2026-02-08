"""
Tests for dict .toCodeDeployConfig() method - format as CodeDeploy config.
"""

from silk.interpreter import Interpreter


class TestDictToCodeDeployConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCodeDeployConfig_basic(self):
        output = self._run('print({"app": "web"}.toCodeDeployConfig())')
        assert output[-1] == "app = web"

    def test_toCodeDeployConfig_multi(self):
        output = self._run('print({"strategy": "rolling", "batch": 25}.toCodeDeployConfig())')
        assert "batch = 25" in output[-1]
