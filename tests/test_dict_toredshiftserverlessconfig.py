"""
Tests for dict .toRedshiftServerlessConfig() method - format as Redshift Serverless config.
"""

from silk.interpreter import Interpreter


class TestDictToRedshiftServerlessConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshiftServerlessConfig_basic(self):
        output = self._run('print({"namespace": "analytics"}.toRedshiftServerlessConfig())')
        assert output[-1] == "namespace = analytics"

    def test_toRedshiftServerlessConfig_multi(self):
        output = self._run('print({"rpu": 128, "base_capacity": 32}.toRedshiftServerlessConfig())')
        assert "rpu = 128" in output[-1]
