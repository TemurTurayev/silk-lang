"""
Tests for dict .toEMRServerlessConfig() method - format as EMR Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToEMRServerlessConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMRServerlessConfig_basic(self):
        output = self._run('print({"runtime": "spark"}.toEMRServerlessConfig())')
        assert output[-1] == "runtime = spark"

    def test_toEMRServerlessConfig_multi(self):
        output = self._run('print({"cpu": 4, "memory": 16}.toEMRServerlessConfig())')
        assert "cpu = 4" in output[-1]
