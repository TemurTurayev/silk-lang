"""
Tests for dict .toMacieConfig() method - format as Macie config.
"""

from silk.interpreter import Interpreter


class TestDictToMacieConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMacieConfig_basic(self):
        output = self._run('print({"bucket": "data-lake"}.toMacieConfig())')
        assert output[-1] == "bucket = data-lake"

    def test_toMacieConfig_multi(self):
        output = self._run('print({"scan": "enabled", "frequency": "daily"}.toMacieConfig())')
        assert "scan = enabled" in output[-1]
