"""
Tests for dict .maxValue() and .minValue() methods.
"""

from silk.interpreter import Interpreter


class TestDictMaxMinValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_maxValue_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3}
print(d.maxValue())
''')
        assert output[-1] == '5'

    def test_minValue_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3}
print(d.minValue())
''')
        assert output[-1] == '1'
