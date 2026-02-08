"""
Tests for dict .toCostExplorerConfig() method - format as Cost Explorer config.
"""

from silk.interpreter import Interpreter


class TestDictToCostExplorerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCostExplorerConfig_basic(self):
        output = self._run('print({"granularity": "daily"}.toCostExplorerConfig())')
        assert output[-1] == "granularity = daily"

    def test_toCostExplorerConfig_multi(self):
        output = self._run('print({"metric": "cost", "group": "service"}.toCostExplorerConfig())')
        assert "metric = cost" in output[-1]
