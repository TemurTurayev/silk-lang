"""
Tests for dict .toTextractConfig() method - format as Textract config.
"""

from silk.interpreter import Interpreter


class TestDictToTextractConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTextractConfig_basic(self):
        output = self._run('print({"feature": "tables"}.toTextractConfig())')
        assert output[-1] == "feature = tables"

    def test_toTextractConfig_multi(self):
        output = self._run('print({"bucket": "docs", "pages": 10}.toTextractConfig())')
        assert "bucket = docs" in output[-1]
