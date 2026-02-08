"""
Tests for number .digitTrimmedMean() method - mean after removing min and max digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrimmedMean:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrimmedMean_equal(self):
        output = self._run('print(333.digitTrimmedMean())')
        assert output[-1] == "3"

    def test_digitTrimmedMean_varied(self):
        output = self._run('print(1234.digitTrimmedMean())')
        # sorted: 1,2,3,4 => trim min(1) and max(4) => mean(2,3)=2.5
        assert output[-1] == "2.5"
