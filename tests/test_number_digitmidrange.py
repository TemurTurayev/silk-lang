"""
Tests for number .digitMidrange() method - average of min and max digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMidrange:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMidrange_equal(self):
        output = self._run('print(333.digitMidrange())')
        assert output[-1] == "3"

    def test_digitMidrange_varied(self):
        output = self._run('print(19.digitMidrange())')
        # midrange(1,9) = (1+9)/2 = 5
        assert output[-1] == "5"
