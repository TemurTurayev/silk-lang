"""
Tests for dict .deepGet(path) method.
"""

from silk.interpreter import Interpreter


class TestDictDeepGet:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_deepGet_nested(self):
        output = self._run('''
let d = {"a": {"b": {"c": 42}}}
print(d.deepGet("a.b.c"))
''')
        assert output[-1] == "42"

    def test_deepGet_shallow(self):
        output = self._run('''
let d = {"x": 10}
print(d.deepGet("x"))
''')
        assert output[-1] == "10"

    def test_deepGet_missing(self):
        output = self._run('''
let d = {"a": 1}
print(d.deepGet("b"))
''')
        assert output[-1] == "null"
