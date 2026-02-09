"""
Tests for number .digitQuattuortrigintSum() method - sum of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintSum_basic(self):
        output = self._run('print(1111111111111111111111111111111111.digitQuattuortrigintSum())')
        assert output[-1] == "[34]"

    def test_digitQuattuortrigintSum_remainder(self):
        output = self._run('print(11111111111111111111111111111111115.digitQuattuortrigintSum())')
        assert output[-1] == "[34, 5]"
