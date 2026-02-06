"""
Tests for number .aliquotSum() method.
"""

from silk.interpreter import Interpreter


class TestNumberAliquotSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_aliquotSum_12(self):
        output = self._run('print(12.aliquotSum())')
        assert output[-1] == "16"

    def test_aliquotSum_perfect(self):
        output = self._run('print(6.aliquotSum())')
        assert output[-1] == "6"

    def test_aliquotSum_prime(self):
        output = self._run('print(7.aliquotSum())')
        assert output[-1] == "1"
