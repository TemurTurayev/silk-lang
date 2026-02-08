"""
Tests for dict .toMariaDBConfig() method - MariaDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToMariaDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMariaDBConfig_basic(self):
        output = self._run('''
let d = {"bind_address": "0.0.0.0"}
print(d.toMariaDBConfig())
''')
        assert output[-1] == "bind_address = 0.0.0.0"

    def test_toMariaDBConfig_number(self):
        output = self._run('''
let d = {"max_connections": 100}
print(d.toMariaDBConfig())
''')
        assert output[-1] == "max_connections = 100"
