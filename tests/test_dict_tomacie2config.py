"""
Tests for dict .toMacie2Config() method - format as Macie v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMacie2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMacie2Config_basic(self):
        output = self._run('print({"bucket": "data-store"}.toMacie2Config())')
        assert output[-1] == "bucket = data-store"

    def test_toMacie2Config_multi(self):
        output = self._run('print({"bucket": "data-store", "status": "enabled"}.toMacie2Config())')
        assert output[-1] == "bucket = data-store\nstatus = enabled"
