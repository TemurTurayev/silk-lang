"""
Tests for number .bigOmega() method - count of prime factors with multiplicity.
"""

from silk.interpreter import Interpreter


class TestNumberBigOmega:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_bigOmega_12(self):
        output = self._run('print(12.bigOmega())')
        assert output[-1] == "3"

    def test_bigOmega_30(self):
        output = self._run('print(30.bigOmega())')
        assert output[-1] == "3"
