"""
Tests for dict .toHelmChartConfig() method - Helm chart config format.
"""

from silk.interpreter import Interpreter


class TestDictToHelmChartConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHelmChartConfig_basic(self):
        output = self._run('print({"replica": 3}.toHelmChartConfig())')
        assert output[-1] == "replica = 3"

    def test_toHelmChartConfig_multi(self):
        output = self._run('print({"replica": 3, "name": "web"}.toHelmChartConfig())')
        assert "replica = 3" in output[-1]
        assert "name = web" in output[-1]
