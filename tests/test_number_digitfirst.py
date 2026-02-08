"""
Tests for number .digitFirst() method - return first digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitFirst_basic(self):
        output = self._run('print(12345.digitFirst())')
        assert output[-1] == "1"

    def test_digitFirst_single(self):
        output = self._run('print(7.digitFirst())')
        assert output[-1] == "7"
