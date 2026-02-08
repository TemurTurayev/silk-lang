"""
Tests for dict .toConnectConfig() method - format as Amazon Connect config.
"""

from silk.interpreter import Interpreter


class TestDictToConnectConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConnectConfig_basic(self):
        output = self._run('print({"instance": "main"}.toConnectConfig())')
        assert output[-1] == "instance = main"

    def test_toConnectConfig_multi(self):
        output = self._run('print({"instance": "main", "region": "us-east-1"}.toConnectConfig())')
        assert "instance = main" in output[-1]
