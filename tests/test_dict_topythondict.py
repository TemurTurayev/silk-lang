"""
Tests for dict .toPythonDict() method.
"""

from silk.interpreter import Interpreter


class TestDictToPythonDict:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPythonDict_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let py = d.toPythonDict()
print(py.contains(":"))
''')
        assert output[-1] == "true"

    def test_toPythonDict_braces(self):
        output = self._run('''
let d = {"x": 1}
let py = d.toPythonDict()
print(py.starts_with("{"))
''')
        assert output[-1] == "true"
