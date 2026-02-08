"""
Tests for dict .toChimeConfig() method - format as Amazon Chime config.
"""

from silk.interpreter import Interpreter


class TestDictToChimeConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toChimeConfig_basic(self):
        output = self._run('print({"account": "main"}.toChimeConfig())')
        assert output[-1] == "account = main"

    def test_toChimeConfig_multi(self):
        output = self._run('print({"account": "main", "region": "us-east-1"}.toChimeConfig())')
        assert "account = main" in output[-1]
