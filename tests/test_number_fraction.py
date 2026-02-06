"""
Tests for number .toFraction() method.
"""

from silk.interpreter import Interpreter


class TestNumberToFraction:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFraction_half(self):
        output = self._run('print(0.5.toFraction())')
        assert output[-1] == "1/2"

    def test_toFraction_third(self):
        output = self._run('print(0.75.toFraction())')
        assert output[-1] == "3/4"

    def test_toFraction_integer(self):
        output = self._run('print(3.toFraction())')
        assert output[-1] == "3"
