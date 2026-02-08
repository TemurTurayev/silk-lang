"""
Tests for dict .toArangoDBConfig() method - ArangoDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToArangoDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toArangoDBConfig_basic(self):
        output = self._run('''
let d = {"endpoint": "tcp://127.0.0.1:8529"}
print(d.toArangoDBConfig())
''')
        assert output[-1] == 'endpoint = tcp://127.0.0.1:8529'

    def test_toArangoDBConfig_number(self):
        output = self._run('''
let d = {"threads": 4}
print(d.toArangoDBConfig())
''')
        assert output[-1] == 'threads = 4'
