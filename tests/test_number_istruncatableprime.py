"""
Tests for number .isTruncatablePrime() method - right-truncatable prime.
"""

from silk.interpreter import Interpreter


class TestNumberIsTruncatablePrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isTruncatablePrime_37(self):
        output = self._run('print(37.isTruncatablePrime())')
        assert output[-1] == "true"

    def test_isTruncatablePrime_23(self):
        output = self._run('print(23.isTruncatablePrime())')
        assert output[-1] == "true"

    def test_isTruncatablePrime_19(self):
        output = self._run('print(19.isTruncatablePrime())')
        assert output[-1] == "false"
