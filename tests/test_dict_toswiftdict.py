"""
Tests for dict .toSwiftDict() method.
"""

from silk.interpreter import Interpreter


class TestDictToSwiftDict:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSwiftDict_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let sw = d.toSwiftDict()
print(sw.contains(":"))
''')
        assert output[-1] == "true"

    def test_toSwiftDict_brackets(self):
        output = self._run('''
let d = {"x": 1}
let sw = d.toSwiftDict()
print(sw.starts_with("["))
''')
        assert output[-1] == "true"
