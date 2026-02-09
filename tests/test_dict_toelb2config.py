"""
Tests for dict .toELB2Config() method - format as ELB v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToELB2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toELB2Config_basic(self):
        output = self._run('print({"type": "application"}.toELB2Config())')
        assert output[-1] == "type = application"

    def test_toELB2Config_multi(self):
        output = self._run('print({"type": "application", "port": 443}.toELB2Config())')
        assert output[-1] == "type = application\nport = 443"
