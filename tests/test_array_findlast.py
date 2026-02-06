"""
Tests for array .findLast() and .findLastIndex() methods.
"""

from silk.interpreter import Interpreter


class TestArrayFindLast:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_findLast_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].findLast(|x| x % 2 == 0))
''')
        assert output[-1] == "4"

    def test_findLast_not_found(self):
        output = self._run('''
print([1, 3, 5].findLast(|x| x % 2 == 0))
''')
        assert output[-1] == "null"

    def test_findLastIndex_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].findLastIndex(|x| x % 2 == 0))
''')
        assert output[-1] == "3"

    def test_findLastIndex_not_found(self):
        output = self._run('''
print([1, 3, 5].findLastIndex(|x| x % 2 == 0))
''')
        assert output[-1] == "-1"
