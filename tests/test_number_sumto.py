"""
Tests for number .sumTo() method.
"""

from silk.interpreter import Interpreter


class TestNumberSumTo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sumTo_basic(self):
        output = self._run('print(10.sumTo())')
        assert output[-1] == "55"

    def test_sumTo_one(self):
        output = self._run('print(1.sumTo())')
        assert output[-1] == "1"

    def test_sumTo_hundred(self):
        output = self._run('print(100.sumTo())')
        assert output[-1] == "5050"
