"""
Tests for dict .toTextract2Config() method - format as Textract v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToTextract2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTextract2Config_basic(self):
        output = self._run('print({"feature": "TABLES"}.toTextract2Config())')
        assert output[-1] == "feature = TABLES"

    def test_toTextract2Config_multi(self):
        output = self._run('print({"feature": "TABLES", "bucket": "docs"}.toTextract2Config())')
        assert output[-1] == "feature = TABLES\nbucket = docs"
