"""
Tests for array .dropWhileRight(fn) method - drop from right while predicate holds.
"""

from silk.interpreter import Interpreter


class TestArrayDropWhileRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dropWhileRight_gt2(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].dropWhileRight(|x| x > 2)
print(result)
''')
        assert output[-1] == "[1, 2]"

    def test_dropWhileRight_even(self):
        output = self._run('''
let result = [1, 3, 2, 4].dropWhileRight(|x| x % 2 == 0)
print(result)
''')
        assert output[-1] == "[1, 3]"
