"""
Tests for number .digitSum() method.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSum_basic(self):
        output = self._run('print(123.digitSum())')
        assert output[-1] == "6"

    def test_digitSum_single(self):
        output = self._run('print(7.digitSum())')
        assert output[-1] == "7"

    def test_digitSum_large(self):
        output = self._run('print(9999.digitSum())')
        assert output[-1] == "36"

    def test_digitSum_zero(self):
        output = self._run('print(0.digitSum())')
        assert output[-1] == "0"
