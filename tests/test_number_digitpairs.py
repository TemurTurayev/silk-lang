"""
Tests for number .digitPairs() method - consecutive digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairs_basic(self):
        output = self._run('print(1234.digitPairs())')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_digitPairs_two_digits(self):
        output = self._run('print(42.digitPairs())')
        assert output[-1] == "[[4, 2]]"
