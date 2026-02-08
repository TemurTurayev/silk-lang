"""
Tests for dict .toLokiConfig() method - Loki config format.
"""

from silk.interpreter import Interpreter


class TestDictToLokiConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLokiConfig_basic(self):
        output = self._run('print({"port": 3100}.toLokiConfig())')
        assert output[-1] == "port = 3100"

    def test_toLokiConfig_multi(self):
        output = self._run('print({"port": 3100, "host": "0.0.0.0"}.toLokiConfig())')
        assert "port = 3100" in output[-1]
        assert "host = 0.0.0.0" in output[-1]
