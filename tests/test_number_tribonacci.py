"""
Tests for number .tribonacci() method.
"""

from silk.interpreter import Interpreter


class TestNumberTribonacci:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_tribonacci_0(self):
        output = self._run('print(0.tribonacci())')
        assert output[-1] == "0"

    def test_tribonacci_3(self):
        output = self._run('print(3.tribonacci())')
        assert output[-1] == "2"

    def test_tribonacci_7(self):
        output = self._run('print(7.tribonacci())')
        assert output[-1] == "24"
