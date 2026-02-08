"""
Tests for dict .toOrientDBConfig() method - OrientDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToOrientDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOrientDBConfig_basic(self):
        output = self._run('''
let d = {"server.database.path": "/data"}
print(d.toOrientDBConfig())
''')
        assert output[-1] == 'server.database.path = /data'

    def test_toOrientDBConfig_number(self):
        output = self._run('''
let d = {"network.port": 2424}
print(d.toOrientDBConfig())
''')
        assert output[-1] == 'network.port = 2424'
