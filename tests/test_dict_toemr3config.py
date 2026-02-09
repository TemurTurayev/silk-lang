"""
Tests for dict .toEMR3Config() method - format as EMR v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToEMR3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toEMR3Config_basic(self):
        output = self._run('print({"cluster": "analytics"}.toEMR3Config())')
        assert output[-1] == "cluster = analytics"

    def test_toEMR3Config_multi(self):
        output = self._run('print({"cluster": "analytics", "releaseLabel": "emr-6.9.0"}.toEMR3Config())')
        assert output[-1] == "cluster = analytics\nreleaseLabel = emr-6.9.0"
