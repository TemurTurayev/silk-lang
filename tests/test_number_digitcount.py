"""
Tests for number .digitCount() method.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCount_single(self):
        output = self._run('print(7.digitCount())')
        assert output[-1] == "1"

    def test_digitCount_multi(self):
        output = self._run('print(12345.digitCount())')
        assert output[-1] == "5"

    def test_digitCount_zero(self):
        output = self._run('print(0.digitCount())')
        assert output[-1] == "1"
