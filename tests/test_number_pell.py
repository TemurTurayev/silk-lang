"""
Tests for number .pell() method - Pell number.
"""

from silk.interpreter import Interpreter


class TestNumberPell:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pell_0(self):
        output = self._run('print(0.pell())')
        assert output[-1] == "0"

    def test_pell_4(self):
        output = self._run('print(4.pell())')
        assert output[-1] == "12"

    def test_pell_6(self):
        output = self._run('print(6.pell())')
        assert output[-1] == "70"
