"""
Tests for dict .toMakefileVars() method - convert dict to Makefile variable format.
"""

from silk.interpreter import Interpreter


class TestDictToMakefileVars:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMakefileVars_basic(self):
        output = self._run('''
let d = {"CC": "gcc"}
print(d.toMakefileVars())
''')
        assert output[-1] == 'CC := gcc'

    def test_toMakefileVars_number(self):
        output = self._run('''
let d = {"PORT": 8080}
print(d.toMakefileVars())
''')
        assert output[-1] == 'PORT := 8080'
