"""
Tests for dict .toNetworkFirewall2Config() method - format as NetworkFirewall v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToNetworkFirewall2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNetworkFirewall2Config_basic(self):
        output = self._run('print({"rule_group": "stateful"}.toNetworkFirewall2Config())')
        assert output[-1] == "rule_group = stateful"

    def test_toNetworkFirewall2Config_multi(self):
        output = self._run('print({"rule_group": "stateful", "priority": "100"}.toNetworkFirewall2Config())')
        assert output[-1] == "rule_group = stateful\npriority = 100"
