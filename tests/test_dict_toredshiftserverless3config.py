"""
Tests for dict .toRedshiftServerless3Config() method - format as Redshift Serverless v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToRedshiftServerless3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRedshiftServerless3Config_basic(self):
        output = self._run('print({"namespace": "analytics"}.toRedshiftServerless3Config())')
        assert output[-1] == "namespace = analytics"

    def test_toRedshiftServerless3Config_multi(self):
        output = self._run('print({"namespace": "analytics", "rpu": 128}.toRedshiftServerless3Config())')
        assert output[-1] == "namespace = analytics\nrpu = 128"
