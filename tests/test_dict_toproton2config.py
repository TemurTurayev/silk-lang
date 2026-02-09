"""
Tests for dict .toProton2Config() method - format as Proton v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToProton2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toProton2Config_basic(self):
        output = self._run('print({"service": "myService"}.toProton2Config())')
        assert output[-1] == "service = myService"

    def test_toProton2Config_multi(self):
        output = self._run('print({"service": "api", "environment": "prod"}.toProton2Config())')
        assert output[-1] == "service = api\nenvironment = prod"
