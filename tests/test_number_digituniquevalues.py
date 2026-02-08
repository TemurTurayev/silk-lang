"""
Tests for number .digitUniqueValues() method - get sorted unique digit values.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUniqueValues:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUniqueValues_basic(self):
        output = self._run('print(112234.digitUniqueValues())')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_digitUniqueValues_all_same(self):
        output = self._run('print(5555.digitUniqueValues())')
        assert output[-1] == "[5]"
