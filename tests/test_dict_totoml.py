"""
Tests for dict .toTOML() method.
"""

from silk.interpreter import Interpreter


class TestDictToTOML:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTOML_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toTOML())
''')
        assert output[-1] == 'name = "Bob"'

    def test_toTOML_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toTOML())
''')
        assert output[-1] == "port = 8080"
