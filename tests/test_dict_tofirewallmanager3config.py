"""
Tests for dict .toFirewallManager3Config() method - format dict as FirewallManager3 config.
"""

from silk.interpreter import Interpreter


class TestDictToFirewallManager3Config:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFirewallManager3Config_basic(self):
        output = self._run('print({"host": "localhost"}.toFirewallManager3Config())')
        assert output[-1] == "host = localhost"

    def test_toFirewallManager3Config_multi(self):
        output = self._run('print({"host": "localhost", "port": 443}.toFirewallManager3Config())')
        assert output[-1] == "host = localhost\nport = 443"
