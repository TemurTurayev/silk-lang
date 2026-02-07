"""
Tests for dict .deepSet(path, value) method.
"""

from silk.interpreter import Interpreter


class TestDictDeepSet:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_deepSet_nested(self):
        output = self._run('''
let d = {"a": {"b": 1}}
let r = d.deepSet("a.b", 42)
print(r.deepGet("a.b"))
''')
        assert output[-1] == "42"

    def test_deepSet_shallow(self):
        output = self._run('''
let d = {"x": 1}
let r = d.deepSet("x", 99)
print(r)
''')
        assert output[-1] == '{"x": 99}'

    def test_deepSet_creates_path(self):
        output = self._run('''
let d = {"a": 1}
let r = d.deepSet("b.c", 5)
print(r.deepGet("b.c"))
''')
        assert output[-1] == "5"
