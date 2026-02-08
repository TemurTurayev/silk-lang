"""
Tests for dict .toAlloyConfig() method - format as Alloy config.
"""

from silk.interpreter import Interpreter


class TestDictToAlloyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAlloyConfig_basic(self):
        output = self._run('print({"server": "main"}.toAlloyConfig())')
        assert output[-1] == "server = main"

    def test_toAlloyConfig_multi(self):
        output = self._run('print({"port": 12345, "active": true}.toAlloyConfig())')
        assert "active = true" in output[-1]
