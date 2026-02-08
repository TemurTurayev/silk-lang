"""
Tests for array .mapScan(init, fn) method - scan with accumulator.
"""

from silk.interpreter import Interpreter


class TestArrayMapScan:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapScan_sum(self):
        output = self._run('''
let result = [1, 2, 3].mapScan(0, |a, x| a + x)
print(result)
''')
        assert output[-1] == "[1, 3, 6]"

    def test_mapScan_multiply(self):
        output = self._run('''
let result = [2, 3, 4].mapScan(1, |a, x| a * x)
print(result)
''')
        assert output[-1] == "[2, 6, 24]"
