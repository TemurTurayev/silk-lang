"""
Tests for dict .toFirewallManagerConfig() method - format as Firewall Manager config.
"""

from silk.interpreter import Interpreter


class TestDictToFirewallManagerConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFirewallManagerConfig_basic(self):
        output = self._run('print({"policy": "default"}.toFirewallManagerConfig())')
        assert output[-1] == "policy = default"

    def test_toFirewallManagerConfig_multi(self):
        output = self._run('print({"scope": "org", "type": "waf"}.toFirewallManagerConfig())')
        assert "scope = org" in output[-1]
