"""
Tests for dict .toTextract3Config() method - format as Textract v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTextract3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTextract3Config_basic(self):
        output = self._run('print({"feature": "TABLES"}.toTextract3Config())')
        assert output[-1] == "feature = TABLES"

    def test_toTextract3Config_multi(self):
        output = self._run('print({"feature": "TABLES", "format": "csv"}.toTextract3Config())')
        assert output[-1] == "feature = TABLES\nformat = csv"
