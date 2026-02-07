"""
Tests for dict .toProperties() method - Java properties format.
"""

from silk.interpreter import Interpreter


class TestDictToProperties:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toProperties_basic(self):
        output = self._run('''
let d = {"host": "localhost"}
print(d.toProperties())
''')
        assert output[-1] == "host=localhost"

    def test_toProperties_multi(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let p = d.toProperties()
print(p.contains("="))
''')
        assert output[-1] == "true"
