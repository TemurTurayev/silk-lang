"""
Tests for dict .toAppRunner3Config() method - format as App Runner v3 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppRunner3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppRunner3Config_basic(self):
        output = self._run('print({"service": "web"}.toAppRunner3Config())')
        assert output[-1] == "service = web"

    def test_toAppRunner3Config_multi(self):
        output = self._run('print({"service": "web", "port": 8080}.toAppRunner3Config())')
        assert output[-1] == "service = web\nport = 8080"
