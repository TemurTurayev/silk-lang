"""
Tests for dict .toGrafanaLabels() method - Grafana labels format.
"""

from silk.interpreter import Interpreter


class TestDictToGrafanaLabels:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toGrafanaLabels_basic(self):
        output = self._run('print({"env": "prod"}.toGrafanaLabels())')
        assert output[-1] == "env = prod"

    def test_toGrafanaLabels_multi(self):
        output = self._run('print({"env": "prod", "tier": "web"}.toGrafanaLabels())')
        assert "env = prod" in output[-1]
        assert "tier = web" in output[-1]
