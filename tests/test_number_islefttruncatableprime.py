"""
Tests for number .isLeftTruncatablePrime() method - left-truncatable prime.
"""

from silk.interpreter import Interpreter


class TestNumberIsLeftTruncatablePrime:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isLeftTruncatablePrime_37(self):
        output = self._run('print(37.isLeftTruncatablePrime())')
        assert output[-1] == "true"

    def test_isLeftTruncatablePrime_53(self):
        output = self._run('print(53.isLeftTruncatablePrime())')
        assert output[-1] == "true"

    def test_isLeftTruncatablePrime_19(self):
        output = self._run('print(19.isLeftTruncatablePrime())')
        assert output[-1] == "false"
