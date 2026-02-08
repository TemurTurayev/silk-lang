"""
Tests for dict .toBigtableConfig() method - Bigtable config format.
"""

from silk.interpreter import Interpreter


class TestDictToBigtableConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBigtableConfig_basic(self):
        output = self._run('print({"nodes": 5}.toBigtableConfig())')
        assert output[-1] == "nodes = 5"

    def test_toBigtableConfig_string(self):
        output = self._run('print({"project": "myproj"}.toBigtableConfig())')
        assert output[-1] == "project = myproj"
