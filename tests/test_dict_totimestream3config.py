"""
Tests for dict .toTimestream3Config() method - format as Timestream v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTimestream3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTimestream3Config_basic(self):
        output = self._run('print({"database": "metrics"}.toTimestream3Config())')
        assert output[-1] == "database = metrics"

    def test_toTimestream3Config_multi(self):
        output = self._run('print({"database": "metrics", "retention": 365}.toTimestream3Config())')
        assert output[-1] == "database = metrics\nretention = 365"
