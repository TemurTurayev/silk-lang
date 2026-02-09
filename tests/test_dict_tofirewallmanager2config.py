"""
Tests for dict .toFirewallManager2Config() method - format as FirewallManager v2 config (Grafana-style).
"""

from silk.interpreter import Interpreter


class TestDictToFirewallManager2Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFirewallManager2Config_basic(self):
        output = self._run('print({"policy": "default"}.toFirewallManager2Config())')
        assert output[-1] == "policy = default"

    def test_toFirewallManager2Config_multi(self):
        output = self._run('print({"policy": "default", "scope": "global"}.toFirewallManager2Config())')
        assert output[-1] == "policy = default\nscope = global"
