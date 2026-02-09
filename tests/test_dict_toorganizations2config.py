"""
Tests for dict .toOrganizations2Config() method - format as Organizations v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToOrganizations2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOrganizations2Config_basic(self):
        output = self._run('print({"ou": "production"}.toOrganizations2Config())')
        assert output[-1] == "ou = production"

    def test_toOrganizations2Config_multi(self):
        output = self._run('print({"ou": "production", "scp": "deny-all"}.toOrganizations2Config())')
        assert output[-1] == "ou = production\nscp = deny-all"
