"""
Tests for number .digitWinsorizedMean() method - mean with min/max replaced by nearest values.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWinsorizedMean:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWinsorizedMean_equal(self):
        output = self._run('print(333.digitWinsorizedMean())')
        assert output[-1] == "3"

    def test_digitWinsorizedMean_varied(self):
        output = self._run('print(1234.digitWinsorizedMean())')
        # sorted: 1,2,3,4 => winsorized: 2,2,3,3 => mean=2.5
        assert output[-1] == "2.5"
