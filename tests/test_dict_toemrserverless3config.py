"""
Tests for dict .toEMRServerless3Config() method - format as EMR Serverless v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToEMRServerless3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMRServerless3Config_basic(self):
        output = self._run('print({"runtime": "spark"}.toEMRServerless3Config())')
        assert output[-1] == "runtime = spark"

    def test_toEMRServerless3Config_multi(self):
        output = self._run('print({"runtime": "spark", "workers": 10}.toEMRServerless3Config())')
        assert output[-1] == "runtime = spark\nworkers = 10"
