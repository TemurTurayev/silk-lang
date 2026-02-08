"""
Tests for dict .toAgentConfig() method - format as agent config.
"""

from silk.interpreter import Interpreter


class TestDictToAgentConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAgentConfig_basic(self):
        output = self._run('print({"name": "collector"}.toAgentConfig())')
        assert output[-1] == "name = collector"

    def test_toAgentConfig_multi(self):
        output = self._run('print({"port": 8080, "debug": false}.toAgentConfig())')
        assert "debug = false" in output[-1]
