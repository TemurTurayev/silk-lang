"""
Tests for number .digitGap() method - max difference between consecutive digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitGap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitGap_1928(self):
        output = self._run('print(1928.digitGap())')
        assert output[-1] == "8"

    def test_digitGap_1234(self):
        output = self._run('print(1234.digitGap())')
        assert output[-1] == "1"
