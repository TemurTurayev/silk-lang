"""
Tests for dict .intersectKeys(other) method.
"""

from silk.interpreter import Interpreter


class TestDictIntersectKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_intersectKeys_basic(self):
        output = self._run('''
let a = {"x": 1, "y": 2, "z": 3}
let b = {"y": 99, "z": 88}
let r = a.intersectKeys(b)
print(r)
''')
        assert output[-1] == '{"y": 2, "z": 3}'

    def test_intersectKeys_no_overlap(self):
        output = self._run('''
let a = {"a": 1}
let b = {"b": 2}
print(a.intersectKeys(b).isEmpty())
''')
        assert output[-1] == "true"
