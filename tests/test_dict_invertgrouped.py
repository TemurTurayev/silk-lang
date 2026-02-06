"""
Tests for dict .invertGrouped() method.
"""

from silk.interpreter import Interpreter


class TestDictInvertGrouped:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_invertGrouped_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1}
let ig = d.invertGrouped()
print(ig[1])
print(ig[2])
''')
        assert output[0] == "[a, c]"
        assert output[1] == "[b]"

    def test_invertGrouped_unique(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
let ig = d.invertGrouped()
print(ig[10])
''')
        assert output[-1] == "[x]"
