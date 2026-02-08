"""
Tests for dict .toMongoConfig() method - MongoDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToMongoConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMongoConfig_basic(self):
        output = self._run('''
let d = {"port": 27017}
print(d.toMongoConfig())
''')
        assert output[-1] == 'port: 27017'

    def test_toMongoConfig_string(self):
        output = self._run('''
let d = {"bindIp": "127.0.0.1"}
print(d.toMongoConfig())
''')
        assert output[-1] == 'bindIp: 127.0.0.1'
