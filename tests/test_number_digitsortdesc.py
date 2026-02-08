"""
Tests for number .digitSortDesc() method - sort digits descending.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSortDesc:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSortDesc_basic(self):
        output = self._run('print(5312.digitSortDesc())')
        assert output[-1] == "5321"

    def test_digitSortDesc_repeated(self):
        output = self._run('print(9471.digitSortDesc())')
        assert output[-1] == "9741"
