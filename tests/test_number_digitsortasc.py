"""
Tests for number .digitSortAsc() method - sort digits ascending.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSortAsc:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSortAsc_basic(self):
        output = self._run('print(53142.digitSortAsc())')
        assert output[-1] == "[1, 2, 3, 4, 5]"

    def test_digitSortAsc_repeats(self):
        output = self._run('print(9311.digitSortAsc())')
        assert output[-1] == "[1, 1, 3, 9]"
