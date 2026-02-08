"""
Tests for number .isRegular() method - check if number is a regular number (5-smooth: only 2,3,5 as prime factors).
"""

from silk.interpreter import Interpreter


class TestNumberIsRegular:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isRegular_12(self):
        output = self._run('print(12.isRegular())')
        assert output[-1] == "true"

    def test_isRegular_7(self):
        output = self._run('print(7.isRegular())')
        assert output[-1] == "false"
