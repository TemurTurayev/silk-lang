"""
Tests for number .doubleFactorial() method - n!! = n * (n-2) * (n-4) * ...
"""

from silk.interpreter import Interpreter


class TestNumberDoubleFactorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_doubleFactorial_5(self):
        output = self._run('print(5.doubleFactorial())')
        assert output[-1] == "15"

    def test_doubleFactorial_6(self):
        output = self._run('print(6.doubleFactorial())')
        assert output[-1] == "48"
