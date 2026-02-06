"""
Tests for dict .diffKeys(other) method.
"""

from silk.interpreter import Interpreter


class TestDictDiffKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_diffKeys_basic(self):
        output = self._run('''
let a = {"x": 1, "y": 2, "z": 3}
let b = {"y": 20}
print(a.diffKeys(b))
''')
        assert output[-1] == "[x, z]"

    def test_diffKeys_none(self):
        output = self._run('''
let a = {"x": 1}
let b = {"x": 2}
print(a.diffKeys(b))
''')
        assert output[-1] == "[]"
