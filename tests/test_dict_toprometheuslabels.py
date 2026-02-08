"""
Tests for dict .toPrometheusLabels() method - Prometheus labels format.
"""

from silk.interpreter import Interpreter


class TestDictToPrometheusLabels:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPrometheusLabels_basic(self):
        output = self._run('print({"job": "api"}.toPrometheusLabels())')
        assert output[-1] == "job = api"

    def test_toPrometheusLabels_multi(self):
        output = self._run('print({"job": "api", "port": 9090}.toPrometheusLabels())')
        assert "job = api" in output[-1]
        assert "port = 9090" in output[-1]
