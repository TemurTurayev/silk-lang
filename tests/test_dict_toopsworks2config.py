"""
Tests for dict .toOpsWorks2Config() method - format as OpsWorks v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToOpsWorks2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOpsWorks2Config_basic(self):
        output = self._run('print({"stack": "web"}.toOpsWorks2Config())')
        assert output[-1] == "stack = web"

    def test_toOpsWorks2Config_multi(self):
        output = self._run('print({"stack": "web", "layer": "app"}.toOpsWorks2Config())')
        assert output[-1] == "stack = web\nlayer = app"
