"""
Tests for number .digitWeightedSum() method - sum of digit * position.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWeightedSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWeightedSum_basic(self):
        output = self._run('print(1234.digitWeightedSum())')
        assert output[-1] == "30"

    def test_digitWeightedSum_single(self):
        output = self._run('print(5.digitWeightedSum())')
        assert output[-1] == "5"
