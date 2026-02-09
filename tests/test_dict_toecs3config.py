"""
Tests for dict .toECS3Config() method - format as ECS v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToECS3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toECS3Config_basic(self):
        output = self._run('print({"cluster": "prod"}.toECS3Config())')
        assert output[-1] == "cluster = prod"

    def test_toECS3Config_multi(self):
        output = self._run('print({"cluster": "prod", "service": "web"}.toECS3Config())')
        assert output[-1] == "cluster = prod\nservice = web"
