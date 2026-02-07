"""
Tests for dict .symmetricDifference(other) method.
"""

from silk.interpreter import Interpreter


class TestDictSymmetricDifference:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_symmetricDifference_basic(self):
        output = self._run('''
let a = {"x": 1, "y": 2}
let b = {"y": 3, "z": 4}
let r = a.symmetricDifference(b)
print(r.keys())
''')
        assert output[-1] == "[x, z]"

    def test_symmetricDifference_no_overlap(self):
        output = self._run('''
let a = {"a": 1}
let b = {"b": 2}
let r = a.symmetricDifference(b)
print(r.keys().length)
''')
        assert output[-1] == "2"
