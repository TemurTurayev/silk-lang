"""
Tests for number .isCoprime(n) method.
"""

from silk.interpreter import Interpreter


class TestNumberIsCoprime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCoprime_true(self):
        output = self._run('print(8.isCoprime(15))')
        assert output[-1] == "true"

    def test_isCoprime_false(self):
        output = self._run('print(6.isCoprime(9))')
        assert output[-1] == "false"
