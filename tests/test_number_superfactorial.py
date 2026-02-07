"""
Tests for number .superFactorial() method - product of first n factorials.
"""

from silk.interpreter import Interpreter


class TestNumberSuperFactorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_superFactorial_3(self):
        output = self._run('print(3.superFactorial())')
        assert output[-1] == "12"

    def test_superFactorial_4(self):
        output = self._run('print(4.superFactorial())')
        assert output[-1] == "288"
