"""
Tests for array .takeWhileRight(fn) method - take from right while predicate holds.
"""

from silk.interpreter import Interpreter


class TestArrayTakeWhileRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_takeWhileRight_gt2(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].takeWhileRight(|x| x > 2)
print(result)
''')
        assert output[-1] == "[3, 4, 5]"

    def test_takeWhileRight_even(self):
        output = self._run('''
let result = [1, 3, 2, 4].takeWhileRight(|x| x % 2 == 0)
print(result)
''')
        assert output[-1] == "[2, 4]"
