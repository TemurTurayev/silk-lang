"""
Tests for dict .toRedshiftConfig() method - format as Redshift config.
"""

from silk.interpreter import Interpreter


class TestDictToRedshiftConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshiftConfig_basic(self):
        output = self._run('print({"cluster": "main"}.toRedshiftConfig())')
        assert output[-1] == "cluster = main"

    def test_toRedshiftConfig_multi(self):
        output = self._run('print({"nodes": 4, "type": "dc2"}.toRedshiftConfig())')
        assert "nodes = 4" in output[-1]
