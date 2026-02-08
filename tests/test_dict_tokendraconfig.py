"""
Tests for dict .toKendraConfig() method - format as Kendra config.
"""

from silk.interpreter import Interpreter


class TestDictToKendraConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKendraConfig_basic(self):
        output = self._run('print({"index": "my_index"}.toKendraConfig())')
        assert output[-1] == "index = my_index"

    def test_toKendraConfig_multi(self):
        output = self._run('print({"edition": "enterprise", "capacity": 5}.toKendraConfig())')
        assert "edition = enterprise" in output[-1]
