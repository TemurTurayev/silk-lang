"""
Tests for array .slidingPairs() method - pairs of adjacent elements.
"""

from silk.interpreter import Interpreter


class TestArraySlidingPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_slidingPairs_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4].slidingPairs()
print(result)
''')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_slidingPairs_two(self):
        output = self._run('''
let result = [10, 20].slidingPairs()
print(result)
''')
        assert output[-1] == "[[10, 20]]"
