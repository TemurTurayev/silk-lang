"""
Tests for array .difference() method.
"""

from silk.interpreter import Interpreter


class TestArrayDifference:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_difference_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].difference([2, 4]))
''')
        assert output[-1] == "[1, 3, 5]"

    def test_difference_no_overlap(self):
        output = self._run('''
print([1, 2, 3].difference([4, 5, 6]))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_difference_all(self):
        output = self._run('''
print([1, 2].difference([1, 2, 3]))
''')
        assert output[-1] == "[]"
