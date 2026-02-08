"""
Tests for dict .toCortexConfig() method - format as Cortex config.
"""

from silk.interpreter import Interpreter


class TestDictToCortexConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCortexConfig_basic(self):
        output = self._run('print({"host": "localhost"}.toCortexConfig())')
        assert output[-1] == "host = localhost"

    def test_toCortexConfig_multi(self):
        output = self._run('print({"port": 9009, "enabled": true}.toCortexConfig())')
        assert "enabled = true" in output[-1]
