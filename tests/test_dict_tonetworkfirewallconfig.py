"""
Tests for dict .toNetworkFirewallConfig() method - format as Network Firewall config.
"""

from silk.interpreter import Interpreter


class TestDictToNetworkFirewallConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNetworkFirewallConfig_basic(self):
        output = self._run('print({"vpc": "main"}.toNetworkFirewallConfig())')
        assert output[-1] == "vpc = main"

    def test_toNetworkFirewallConfig_multi(self):
        output = self._run('print({"action": "block", "protocol": "tcp"}.toNetworkFirewallConfig())')
        assert "action = block" in output[-1]
