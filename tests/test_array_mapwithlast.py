"""
Tests for array .mapWithLast(fn) method - map with access to previous result.
"""

from silk.interpreter import Interpreter


class TestArrayMapWithLast:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWithLast_running_sum(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapWithLast(|x, last| x + last)
print(result)
''')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_mapWithLast_double_prev(self):
        output = self._run('''
let result = [10, 20, 30].mapWithLast(|x, last| last * 2)
print(result)
''')
        assert output[-1] == "[10, 20, 40]"
