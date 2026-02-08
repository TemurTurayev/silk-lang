"""
Tests for number .digitEntropy() method - Shannon entropy of digit distribution.
"""

from silk.interpreter import Interpreter


class TestNumberDigitEntropy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitEntropy_uniform(self):
        output = self._run('print(1122.digitEntropy())')
        assert output[-1] == "1"

    def test_digitEntropy_single_digit(self):
        output = self._run('print(1111.digitEntropy())')
        assert output[-1] == "0"
