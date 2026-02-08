"""
Tests for dict .toCouchDBConfig() method - CouchDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToCouchDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCouchDBConfig_basic(self):
        output = self._run('''
let d = {"port": 5984}
print(d.toCouchDBConfig())
''')
        assert output[-1] == 'port = 5984'

    def test_toCouchDBConfig_string(self):
        output = self._run('''
let d = {"bind_address": "127.0.0.1"}
print(d.toCouchDBConfig())
''')
        assert output[-1] == 'bind_address = 127.0.0.1'
