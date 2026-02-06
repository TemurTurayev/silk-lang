"""
Tests for number .isPrime() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsPrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPrime_2(self):
        output = self._run('print(2.isPrime())')
        assert output[-1] == "true"

    def test_isPrime_7(self):
        output = self._run('print(7.isPrime())')
        assert output[-1] == "true"

    def test_isPrime_1(self):
        output = self._run('print(1.isPrime())')
        assert output[-1] == "false"

    def test_isPrime_4(self):
        output = self._run('print(4.isPrime())')
        assert output[-1] == "false"

    def test_isPrime_large(self):
        output = self._run('print(97.isPrime())')
        assert output[-1] == "true"

    def test_isPrime_0(self):
        output = self._run('print(0.isPrime())')
        assert output[-1] == "false"
