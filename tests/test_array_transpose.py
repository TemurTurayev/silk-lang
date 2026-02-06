"""
Tests for array .transpose() method.
"""

from silk.interpreter import Interpreter


class TestArrayTranspose:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_transpose_basic(self):
        output = self._run('''
let m = [[1, 2, 3], [4, 5, 6]]
let t = m.transpose()
print(t[0])
print(t[1])
print(t[2])
''')
        assert output[0] == "[1, 4]"
        assert output[1] == "[2, 5]"
        assert output[2] == "[3, 6]"

    def test_transpose_square(self):
        output = self._run('''
let m = [[1, 2], [3, 4]]
let t = m.transpose()
print(t[0])
print(t[1])
''')
        assert output[0] == "[1, 3]"
        assert output[1] == "[2, 4]"

    def test_transpose_single_row(self):
        output = self._run('''
let t = [[1, 2, 3]].transpose()
print(t.length)
print(t[0])
''')
        assert output[0] == "3"
        assert output[1] == "[1]"
