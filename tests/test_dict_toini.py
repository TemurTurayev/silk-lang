"""
Tests for dict .toINI() method.
"""

from silk.interpreter import Interpreter


class TestDictToINI:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toINI_basic(self):
        output = self._run('''
let d = {"host": "localhost", "port": 8080}
let ini = d.toINI()
print(ini.contains("host=localhost"))
''')
        assert output[-1] == "true"

    def test_toINI_format(self):
        output = self._run('''
let d = {"x": 1}
let ini = d.toINI()
print(ini)
''')
        assert output[-1] == "x=1"
