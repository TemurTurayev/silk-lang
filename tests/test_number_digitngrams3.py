"""
Tests for number .digitNGrams3() method - list of 3-digit n-grams.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNGrams3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNGrams3_basic(self):
        output = self._run('print(12345.digitNGrams3())')
        # [123, 234, 345]
        assert output[-1] == "[123, 234, 345]"

    def test_digitNGrams3_four(self):
        output = self._run('print(1234.digitNGrams3())')
        # [123, 234]
        assert output[-1] == "[123, 234]"
