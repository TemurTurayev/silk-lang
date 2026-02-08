"""
Tests for number .digitAlternatingSum() method - alternating sum of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAlternatingSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAlternatingSum_basic(self):
        output = self._run('print(1234.digitAlternatingSum())')
        assert output[-1] == "-2"

    def test_digitAlternatingSum_three(self):
        output = self._run('print(135.digitAlternatingSum())')
        assert output[-1] == "3"
