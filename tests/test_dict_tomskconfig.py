"""
Tests for dict .toMSKConfig() method - format as Amazon MSK config.
"""

from silk.interpreter import Interpreter


class TestDictToMSKConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMSKConfig_basic(self):
        output = self._run('print({"cluster": "prod"}.toMSKConfig())')
        assert output[-1] == "cluster = prod"

    def test_toMSKConfig_multi(self):
        output = self._run('print({"cluster": "prod", "brokers": "3"}.toMSKConfig())')
        assert "cluster = prod" in output[-1]
