"""
Tests for number .digitMax() method - largest digit.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMax_basic(self):
        output = self._run('print(5312.digitMax())')
        assert output[-1] == "5"

    def test_digitMax_with_nine(self):
        output = self._run('print(9071.digitMax())')
        assert output[-1] == "9"
