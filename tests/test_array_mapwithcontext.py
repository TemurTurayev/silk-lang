"""
Tests for array .mapWithContext(init, fn) method - map with accumulator/context.
"""

from silk.interpreter import Interpreter


class TestArrayMapWithContext:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWithContext_runningSum(self):
        output = self._run('''
let result = [1, 2, 3].mapWithContext(0, |ctx, x| ctx + x)
print(result)
''')
        assert output[-1] == "[1, 3, 6]"

    def test_mapWithContext_count(self):
        output = self._run('''
let result = [10, 20, 30].mapWithContext(0, |ctx, x| ctx + 1)
print(result)
''')
        assert output[-1] == "[1, 2, 3]"
