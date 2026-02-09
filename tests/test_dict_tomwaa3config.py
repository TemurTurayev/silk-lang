"""
Tests for dict .toMWAA3Config() method - format as MWAA v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToMWAA3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMWAA3Config_basic(self):
        output = self._run('print({"environment": "production"}.toMWAA3Config())')
        assert output[-1] == "environment = production"

    def test_toMWAA3Config_multi(self):
        output = self._run('print({"environment": "production", "version": "2.5"}.toMWAA3Config())')
        assert output[-1] == "environment = production\nversion = 2.5"
