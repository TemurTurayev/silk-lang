"""
Tests for dict .toSNSConfig() method - format as SNS config.
"""

from silk.interpreter import Interpreter


class TestDictToSNSConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSNSConfig_basic(self):
        output = self._run('print({"topic": "alerts"}.toSNSConfig())')
        assert output[-1] == "topic = alerts"

    def test_toSNSConfig_multi(self):
        output = self._run('print({"protocol": "email", "endpoint": "test"}.toSNSConfig())')
        assert "endpoint = test" in output[-1]
