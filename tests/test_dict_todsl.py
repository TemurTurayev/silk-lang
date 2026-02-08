"""
Tests for dict .toDSL() method - convert dict to a DSL-style config string.
"""

from silk.interpreter import Interpreter


class TestDictToDSL:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDSL_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toDSL())
''')
        assert output[-1] == 'name "Bob"'

    def test_toDSL_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toDSL())
''')
        assert output[-1] == 'port 8080'
