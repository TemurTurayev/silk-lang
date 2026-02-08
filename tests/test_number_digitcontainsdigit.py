"""
Tests for number .digitContainsDigit(d) method - check if digit d appears in number.
"""

from silk.interpreter import Interpreter


class TestNumberDigitContainsDigit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitContainsDigit_true(self):
        output = self._run('print(12345.digitContainsDigit(3))')
        assert output[-1] == "true"

    def test_digitContainsDigit_false(self):
        output = self._run('print(12345.digitContainsDigit(7))')
        assert output[-1] == "false"
