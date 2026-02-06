"""
Tests for number .fibonacci() method.
"""

from silk.interpreter import Interpreter


class TestNumberFibonacci:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fibonacci_0(self):
        output = self._run('print(0.fibonacci())')
        assert output[-1] == "0"

    def test_fibonacci_1(self):
        output = self._run('print(1.fibonacci())')
        assert output[-1] == "1"

    def test_fibonacci_5(self):
        output = self._run('print(5.fibonacci())')
        assert output[-1] == "5"

    def test_fibonacci_10(self):
        output = self._run('print(10.fibonacci())')
        assert output[-1] == "55"
