"""
Tests for misc small methods: array toString, dict clear.
"""

from silk.interpreter import Interpreter


class TestArrayToString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toString(self):
        output = self._run('''
let s = [1, 2, 3].toString()
print(typeof s)
print(s)
''')
        assert output[-2] == "string"
        assert output[-1] == "[1, 2, 3]"


class TestDictClear:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_clear(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let empty = m.clear()
print(empty.length)
''')
        assert output[-1] == "0"

    def test_clear_returns_dict(self):
        output = self._run('''
let m = {"x": 1}
let e = m.clear()
print(e.has("x"))
''')
        assert output[-1] == "false"
