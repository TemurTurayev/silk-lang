"""
Tests for number .digitKurtosis() method - kurtosis of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitKurtosis:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitKurtosis_equal(self):
        output = self._run('print(333.digitKurtosis())')
        assert output[-1] == "0"

    def test_digitKurtosis_varied(self):
        output = self._run('print(1234.digitKurtosis())')
        # 4 digits, kurtosis will be some float value
        assert float(output[-1]) < 3
