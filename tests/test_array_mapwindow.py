"""
Tests for array .mapWindow(size) method - sliding window of given size.
"""

from silk.interpreter import Interpreter


class TestArrayMapWindow:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWindow_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapWindow(2)
print(result)
''')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_mapWindow_three(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapWindow(3)
print(result)
''')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"
