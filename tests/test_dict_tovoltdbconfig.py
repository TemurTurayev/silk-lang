"""
Tests for dict .toVoltDBConfig() method - VoltDB config format.
"""

from silk.interpreter import Interpreter


class TestDictToVoltDBConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVoltDBConfig_basic(self):
        output = self._run('''
let d = {"host": "localhost"}
print(d.toVoltDBConfig())
''')
        assert output[-1] == 'host = localhost'

    def test_toVoltDBConfig_number(self):
        output = self._run('''
let d = {"port": 21212}
print(d.toVoltDBConfig())
''')
        assert output[-1] == 'port = 21212'
