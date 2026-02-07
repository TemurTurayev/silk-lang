"""
Tests for array .findIndexRight(fn) method - find last matching index.
"""

from silk.interpreter import Interpreter


class TestArrayFindIndexRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_findIndexRight_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].findIndexRight(|x| x < 4)
print(result)
''')
        assert output[-1] == "2"

    def test_findIndexRight_none(self):
        output = self._run('''
let result = [1, 2, 3].findIndexRight(|x| x > 10)
print(result)
''')
        assert output[-1] == "-1"
