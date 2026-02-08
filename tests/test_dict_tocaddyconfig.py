"""
Tests for dict .toCaddyConfig() method - Caddy web server config format.
"""

from silk.interpreter import Interpreter


class TestDictToCaddyConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCaddyConfig_basic(self):
        output = self._run('''
let d = {"host": "localhost"}
print(d.toCaddyConfig())
''')
        assert output[-1] == "host localhost"

    def test_toCaddyConfig_number(self):
        output = self._run('''
let d = {"port": 443}
print(d.toCaddyConfig())
''')
        assert output[-1] == "port 443"
