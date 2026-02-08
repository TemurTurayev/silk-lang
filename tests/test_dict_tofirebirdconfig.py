"""
Tests for dict .toFirebirdConfig() method - Firebird config format.
"""

from silk.interpreter import Interpreter


class TestDictToFirebirdConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFirebirdConfig_basic(self):
        output = self._run('''
let d = {"RemoteServicePort": 3050}
print(d.toFirebirdConfig())
''')
        assert output[-1] == 'RemoteServicePort = 3050'

    def test_toFirebirdConfig_string(self):
        output = self._run('''
let d = {"DatabaseAccess": "Full"}
print(d.toFirebirdConfig())
''')
        assert output[-1] == 'DatabaseAccess = Full'
