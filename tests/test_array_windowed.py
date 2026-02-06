"""
Tests for array .windowed(size) method.
"""

from silk.interpreter import Interpreter


class TestArrayWindowed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_windowed_basic(self):
        output = self._run('''
let w = [1, 2, 3, 4, 5].windowed(3)
print(w.length)
print(w[0])
print(w[1])
print(w[2])
''')
        assert output[-4] == "3"
        assert output[-3] == "[1, 2, 3]"
        assert output[-2] == "[2, 3, 4]"
        assert output[-1] == "[3, 4, 5]"

    def test_windowed_size_equals_length(self):
        output = self._run('''
let w = [1, 2, 3].windowed(3)
print(w.length)
print(w[0])
''')
        assert output[-2] == "1"
        assert output[-1] == "[1, 2, 3]"

    def test_windowed_size_two(self):
        output = self._run('''
let w = [10, 20, 30, 40].windowed(2)
print(w.length)
print(w[0])
''')
        assert output[-2] == "3"
        assert output[-1] == "[10, 20]"
