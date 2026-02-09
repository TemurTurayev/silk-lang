"""
Tests for dict .toTimestream2Config() method - format as Timestream v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTimestream2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTimestream2Config_basic(self):
        output = self._run('print({"database": "myDB"}.toTimestream2Config())')
        assert output[-1] == "database = myDB"

    def test_toTimestream2Config_multi(self):
        output = self._run('print({"database": "metrics", "table": "cpu"}.toTimestream2Config())')
        assert output[-1] == "database = metrics\ntable = cpu"
