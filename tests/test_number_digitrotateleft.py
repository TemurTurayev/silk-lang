"""
Tests for number .digitRotateLeft() method - rotate digits left by 1.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRotateLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRotateLeft_basic(self):
        output = self._run('print(12345.digitRotateLeft())')
        assert output[-1] == "23451"

    def test_digitRotateLeft_two(self):
        output = self._run('print(91.digitRotateLeft())')
        assert output[-1] == "19"
