"""
Tests for dict .toMysqlConfig() method - MySQL config format.
"""

from silk.interpreter import Interpreter


class TestDictToMysqlConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMysqlConfig_basic(self):
        output = self._run('''
let d = {"max_connections": 151}
print(d.toMysqlConfig())
''')
        assert output[-1] == 'max_connections = 151'

    def test_toMysqlConfig_string(self):
        output = self._run('''
let d = {"bind_address": "0.0.0.0"}
print(d.toMysqlConfig())
''')
        assert output[-1] == 'bind_address = 0.0.0.0'
