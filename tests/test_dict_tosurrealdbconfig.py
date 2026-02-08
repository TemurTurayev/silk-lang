"""
Tests for dict .toSurrealDBConfig() method - SurrealDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToSurrealDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSurrealDBConfig_basic(self):
        output = self._run('''
let d = {"bind": "0.0.0.0:8000"}
print(d.toSurrealDBConfig())
''')
        assert output[-1] == 'bind = 0.0.0.0:8000'

    def test_toSurrealDBConfig_number(self):
        output = self._run('''
let d = {"port": 8000}
print(d.toSurrealDBConfig())
''')
        assert output[-1] == 'port = 8000'
