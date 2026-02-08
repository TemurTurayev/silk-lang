"""
Tests for number .digitLCM() method - LCM of all digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitLCM_basic(self):
        output = self._run('print(236.digitLCM())')
        assert output[-1] == "6"

    def test_digitLCM_larger(self):
        output = self._run('print(345.digitLCM())')
        assert output[-1] == "60"
