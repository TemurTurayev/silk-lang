"""
Tests for dict .toGlue3Config() method - format as Glue v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToGlue3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGlue3Config_basic(self):
        output = self._run('print({"database": "catalog"}.toGlue3Config())')
        assert output[-1] == "database = catalog"

    def test_toGlue3Config_multi(self):
        output = self._run('print({"database": "catalog", "crawler": "main"}.toGlue3Config())')
        assert output[-1] == "database = catalog\ncrawler = main"
