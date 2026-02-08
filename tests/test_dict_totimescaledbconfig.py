"""
Tests for dict .toTimescaleDBConfig() method - TimescaleDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToTimescaleDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTimescaleDBConfig_basic(self):
        output = self._run('''
let d = {"port": 5432}
print(d.toTimescaleDBConfig())
''')
        assert output[-1] == "port = 5432"

    def test_toTimescaleDBConfig_string(self):
        output = self._run('''
let d = {"listen_addresses": "localhost"}
print(d.toTimescaleDBConfig())
''')
        assert output[-1] == "listen_addresses = 'localhost'"
