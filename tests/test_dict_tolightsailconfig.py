"""
Tests for dict .toLightsailConfig() method - format as AWS Lightsail config.
"""

from silk.interpreter import Interpreter


class TestDictToLightsailConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLightsailConfig_basic(self):
        output = self._run('print({"instance": "web01"}.toLightsailConfig())')
        assert output[-1] == "instance = web01"

    def test_toLightsailConfig_multi(self):
        output = self._run('print({"instance": "web01", "region": "us-east-1"}.toLightsailConfig())')
        assert "instance = web01" in output[-1]
