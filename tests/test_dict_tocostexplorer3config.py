"""
Tests for dict .toCostExplorer3Config() method - format dict as CostExplorer3 config.
"""

from silk.interpreter import Interpreter


class TestDictToCostExplorer3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCostExplorer3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toCostExplorer3Config())')
        assert output[-1] == "host = localhost"

    def test_toCostExplorer3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toCostExplorer3Config())')
        assert output[-1] == "host = localhost\nport = 443"
