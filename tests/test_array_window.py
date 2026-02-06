"""
Tests for array .rotate() and .window() methods.
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
print([1, 2, 3, 4, 5].rotate(-2))
''')
        assert output[-1] == "[3, 4, 5, 1, 2]"

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


class TestArrayWindow:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_window_basic(self):
        output = self._run('''
let w = [1, 2, 3, 4, 5].window(3)
print(w.length)
print(w[0])
print(w[1])
print(w[2])
''')
        assert output[0] == "3"
        assert output[1] == "[1, 2, 3]"
        assert output[2] == "[2, 3, 4]"
        assert output[3] == "[3, 4, 5]"

    def test_window_size_two(self):
        output = self._run('''
let pairs = [1, 2, 3, 4].window(2)
print(pairs.length)
''')
        assert output[-1] == "3"

    def test_window_full_size(self):
        output = self._run('''
print([1, 2, 3].window(3).length)
''')
        assert output[-1] == "1"
