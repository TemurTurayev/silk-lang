"""
Tests for array .reduceWhile(init, fn) method - reduce while fn returns non-false.
"""

from silk.interpreter import Interpreter


class TestArrayReduceWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reduceWhile_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].reduceWhile(0, |acc, x| acc + x)
print(result)
''')
        assert output[-1] == "15"

    def test_reduceWhile_sum_small(self):
        output = self._run('''
let result = [10, 20, 30].reduceWhile(0, |acc, x| acc + x)
print(result)
''')
        assert output[-1] == "60"
