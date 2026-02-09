"""
Tests for dict .toAppConfig3Config() method - format as AppConfig v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppConfig3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppConfig3Config_basic(self):
        output = self._run('print({"app": "myapp"}.toAppConfig3Config())')
        assert output[-1] == "app = myapp"

    def test_toAppConfig3Config_multi(self):
        output = self._run('print({"app": "myapp", "env": "prod"}.toAppConfig3Config())')
        assert output[-1] == "app = myapp\nenv = prod"
