"""
Tests for array .rotate(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayRotate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_rotate_right(self):
        output = self._run('''
print([1, 2, 3, 4, 5].rotate(2))
''')
        assert output[-1] == "[4, 5, 1, 2, 3]"

    def test_rotate_left(self):
        output = self._run('''
print([1, 2, 3, 4, 5].rotate(-1))
''')
        assert output[-1] == "[2, 3, 4, 5, 1]"

    def test_rotate_zero(self):
        output = self._run('''
print([1, 2, 3].rotate(0))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_rotate_full(self):
        output = self._run('''
print([1, 2, 3].rotate(3))
''')
        assert output[-1] == "[1, 2, 3]"
