"""
Tests for array .mapEvery(n, fn) method - apply fn to every nth element.
"""

from silk.interpreter import Interpreter


class TestArrayMapEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapEvery_second(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapEvery(2, |x| x * 10)
print(result)
''')
        assert output[-1] == "[1, 20, 3, 40, 5]"

    def test_mapEvery_third(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5, 6].mapEvery(3, |x| x * 10)
print(result)
''')
        assert output[-1] == "[1, 2, 30, 4, 5, 60]"
