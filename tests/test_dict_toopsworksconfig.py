"""
Tests for dict .toOpsWorksConfig() method - format as AWS OpsWorks config.
"""

from silk.interpreter import Interpreter


class TestDictToOpsWorksConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOpsWorksConfig_basic(self):
        output = self._run('print({"stack": "main"}.toOpsWorksConfig())')
        assert output[-1] == "stack = main"

    def test_toOpsWorksConfig_multi(self):
        output = self._run('print({"stack": "main", "layer": "app"}.toOpsWorksConfig())')
        assert "stack = main" in output[-1]
