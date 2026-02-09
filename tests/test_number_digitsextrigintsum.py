"""
Tests for number .digitSextrigintSum() method - sum of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintSum())')
        assert output[-1] == "[36]"

    def test_digitSextrigintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111111115.digitSextrigintSum())')
        assert output[-1] == "[36, 5]"
