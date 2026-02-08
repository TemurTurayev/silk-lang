"""
Tests for array .unfold(seed, fn, count) - generate array by unfolding a function.
"""

from silk.interpreter import Interpreter


class TestArrayUnfold:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_unfold_doubles(self):
        output = self._run('''
let result = [].unfold(1, |x| x * 2, 5)
print(result)
''')
        assert output[-1] == "[1, 2, 4, 8, 16]"

    def test_unfold_add(self):
        output = self._run('''
let result = [].unfold(0, |x| x + 3, 4)
print(result)
''')
        assert output[-1] == "[0, 3, 6, 9]"
