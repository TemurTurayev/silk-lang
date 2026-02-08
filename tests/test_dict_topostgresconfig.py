"""
Tests for dict .toPostgresConfig() method - PostgreSQL config format.
"""

from silk.interpreter import Interpreter


class TestDictToPostgresConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPostgresConfig_basic(self):
        output = self._run('''
let d = {"max_connections": 100}
print(d.toPostgresConfig())
''')
        assert output[-1] == "max_connections = 100"

    def test_toPostgresConfig_string(self):
        output = self._run('''
let d = {"listen_addresses": "localhost"}
print(d.toPostgresConfig())
''')
        assert output[-1] == "listen_addresses = 'localhost'"
