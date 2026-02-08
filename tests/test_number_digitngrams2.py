"""
Tests for number .digitNGrams2() method - list of 2-digit n-grams.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNGrams2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNGrams2_basic(self):
        output = self._run('print(1234.digitNGrams2())')
        # [12, 23, 34]
        assert output[-1] == "[12, 23, 34]"

    def test_digitNGrams2_repeating(self):
        output = self._run('print(111.digitNGrams2())')
        # [11, 11]
        assert output[-1] == "[11, 11]"
