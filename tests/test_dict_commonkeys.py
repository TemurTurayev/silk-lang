"""
Tests for dict .commonKeys(other) method.
"""

from silk.interpreter import Interpreter


class TestDictCommonKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_commonKeys_basic(self):
        output = self._run('''
let a = {"x": 1, "y": 2, "z": 3}
let b = {"y": 20, "z": 30, "w": 40}
print(a.commonKeys(b))
''')
        assert output[-1] == "[y, z]"

    def test_commonKeys_none(self):
        output = self._run('''
let a = {"x": 1}
let b = {"y": 2}
print(a.commonKeys(b))
''')
        assert output[-1] == "[]"
