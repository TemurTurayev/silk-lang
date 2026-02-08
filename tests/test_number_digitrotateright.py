"""
Tests for number .digitRotateRight() method - rotate digits right by 1.
"""

from silk.interpreter import Interpreter


class TestNumberDigitRotateRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitRotateRight_basic(self):
        output = self._run('print(12345.digitRotateRight())')
        assert output[-1] == "51234"

    def test_digitRotateRight_two(self):
        output = self._run('print(91.digitRotateRight())')
        assert output[-1] == "19"
