"""
Tests for dict .averageValue() method.
"""

from silk.interpreter import Interpreter


class TestDictAverageValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_averageValue_basic(self):
        output = self._run('''
let d = {"a": 10, "b": 20, "c": 30}
print(d.averageValue())
''')
        assert output[-1] == '20'

    def test_averageValue_decimal(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
print(d.averageValue())
''')
        assert output[-1] == '1.5'
