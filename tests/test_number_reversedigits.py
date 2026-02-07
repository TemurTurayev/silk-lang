"""
Tests for number .reverseDigits() method.
"""

from silk.interpreter import Interpreter


class TestNumberReverseDigits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reverseDigits_basic(self):
        output = self._run('print(123.reverseDigits())')
        assert output[-1] == "321"

    def test_reverseDigits_trailing_zeros(self):
        output = self._run('print(1200.reverseDigits())')
        assert output[-1] == "21"

    def test_reverseDigits_single(self):
        output = self._run('print(5.reverseDigits())')
        assert output[-1] == "5"
