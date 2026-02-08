"""
Tests for array .mapTakeWhile(fn) method - take elements while predicate true.
"""

from silk.interpreter import Interpreter


class TestArrayMapTakeWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTakeWhile_lessThan4(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapTakeWhile(|x| x < 4)
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_mapTakeWhile_all(self):
        output = self._run('''
let result = [1, 2, 3].mapTakeWhile(|x| x < 10)
print(result)
''')
        assert output[-1] == "[1, 2, 3]"
