"""
Tests for array .mapTails() method - all suffixes of the array.
"""

from silk.interpreter import Interpreter


class TestArrayMapTails:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTails_basic(self):
        output = self._run('''
let result = [1, 2, 3].mapTails()
print(result)
''')
        assert output[-1] == "[[1, 2, 3], [2, 3], [3]]"

    def test_mapTails_two(self):
        output = self._run('''
let result = [4, 5].mapTails()
print(result)
''')
        assert output[-1] == "[[4, 5], [5]]"
