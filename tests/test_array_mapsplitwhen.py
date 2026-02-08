"""
Tests for array .mapSplitWhen(fn) method - split array when predicate is true.
"""

from silk.interpreter import Interpreter


class TestArrayMapSplitWhen:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSplitWhen_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapSplitWhen(|x| x == 3)
print(result)
''')
        assert output[-1] == "[[1, 2], [3, 4, 5]]"

    def test_mapSplitWhen_multiple(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5, 6].mapSplitWhen(|x| x == 3)
print(result)
''')
        assert output[-1] == "[[1, 2], [3, 4, 5, 6]]"
