"""
Tests for number .toCurrency() method.
"""

from silk.interpreter import Interpreter


class TestNumberToCurrency:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCurrency_basic(self):
        output = self._run('print(1234.56.toCurrency())')
        assert output[-1] == "$1,234.56"

    def test_toCurrency_round(self):
        output = self._run('print(1000.toCurrency())')
        assert output[-1] == "$1,000.00"

    def test_toCurrency_small(self):
        output = self._run('print(9.99.toCurrency())')
        assert output[-1] == "$9.99"
