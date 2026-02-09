"""
Tests for dict .toAthena3Config() method - format as Athena v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAthena3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAthena3Config_basic(self):
        output = self._run('print({"database": "analytics"}.toAthena3Config())')
        assert output[-1] == "database = analytics"

    def test_toAthena3Config_multi(self):
        output = self._run('print({"database": "analytics", "workgroup": "primary"}.toAthena3Config())')
        assert output[-1] == "database = analytics\nworkgroup = primary"
