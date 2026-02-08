"""
Tests for number .digitUniqueCount() method - count of unique digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUniqueCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUniqueCount_basic(self):
        output = self._run('print(11234.digitUniqueCount())')
        assert output[-1] == "4"

    def test_digitUniqueCount_all_same(self):
        output = self._run('print(1111.digitUniqueCount())')
        assert output[-1] == "1"
