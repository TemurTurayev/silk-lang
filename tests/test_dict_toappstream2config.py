"""
Tests for dict .toAppStream2Config() method - format as AppStream v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToAppStream2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAppStream2Config_basic(self):
        output = self._run('print({"fleet": "default"}.toAppStream2Config())')
        assert output[-1] == "fleet = default"

    def test_toAppStream2Config_multi(self):
        output = self._run('print({"fleet": "default", "type": "ondemand"}.toAppStream2Config())')
        assert output[-1] == "fleet = default\ntype = ondemand"
