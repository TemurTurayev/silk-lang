"""
Tests for dict .toCSharpDict() method.
"""

from silk.interpreter import Interpreter


class TestDictToCSharpDict:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCSharpDict_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
print(d.toCSharpDict())
''')
        assert output[-1] == '{{"name", "Bob"}}'

    def test_toCSharpDict_number(self):
        output = self._run('''
let d = {"port": 8080}
print(d.toCSharpDict())
''')
        assert output[-1] == '{{"port", 8080}}'
