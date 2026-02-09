"""
Tests for dict .toCUR2Config() method - format as CUR v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToCUR2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCUR2Config_basic(self):
        output = self._run('print({"report": "daily"}.toCUR2Config())')
        assert output[-1] == "report = daily"

    def test_toCUR2Config_multi(self):
        output = self._run('print({"report": "daily", "format": "csv"}.toCUR2Config())')
        assert output[-1] == "report = daily\nformat = csv"
