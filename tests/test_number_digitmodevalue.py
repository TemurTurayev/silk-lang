"""
Tests for number .digitModeValue() method - most frequent digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitModeValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitModeValue_basic(self):
        output = self._run('print(11123.digitModeValue())')
        assert output[-1] == "1"

    def test_digitModeValue_single(self):
        output = self._run('print(5.digitModeValue())')
        assert output[-1] == "5"
