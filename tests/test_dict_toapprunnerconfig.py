"""
Tests for dict .toAppRunnerConfig() method - format as App Runner config.
"""

from silk.interpreter import Interpreter


class TestDictToAppRunnerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppRunnerConfig_basic(self):
        output = self._run('print({"service": "web"}.toAppRunnerConfig())')
        assert output[-1] == "service = web"

    def test_toAppRunnerConfig_multi(self):
        output = self._run('print({"port": 8080, "cpu": 1}.toAppRunnerConfig())')
        assert "cpu = 1" in output[-1]
