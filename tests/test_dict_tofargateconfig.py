"""
Tests for dict .toFargateConfig() method - format as Fargate config.
"""

from silk.interpreter import Interpreter


class TestDictToFargateConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFargateConfig_basic(self):
        output = self._run('print({"platform": "linux"}.toFargateConfig())')
        assert output[-1] == "platform = linux"

    def test_toFargateConfig_multi(self):
        output = self._run('print({"cpu": 512, "memory": 1024}.toFargateConfig())')
        assert "memory = 1024" in output[-1]
