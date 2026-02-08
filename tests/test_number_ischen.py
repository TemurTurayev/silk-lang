"""
Tests for number .isChen() method - prime where p+2 is prime or semiprime.
"""

from silk.interpreter import Interpreter


class TestNumberIsChen:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isChen_5(self):
        output = self._run('print(5.isChen())')
        assert output[-1] == "true"

    def test_isChen_4(self):
        output = self._run('print(4.isChen())')
        assert output[-1] == "false"
