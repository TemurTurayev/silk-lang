"""
Tests for dict .valueCounts() method - count occurrences of each value.
"""

from silk.interpreter import Interpreter


class TestDictValueCounts:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_valueCounts_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1}
print(d.valueCounts())
''')
        assert output[-1] == '{1: 2, 2: 1}'

    def test_valueCounts_unique(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
print(d.valueCounts())
''')
        assert output[-1] == '{10: 1, 20: 1}'
