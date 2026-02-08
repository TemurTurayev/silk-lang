"""
Tests for string .toDecimal() method - convert each char to decimal code.
"""

from silk.interpreter import Interpreter


class TestStringToDecimal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecimal_AB(self):
        output = self._run('print("AB".toDecimal())')
        assert output[-1] == "65,66"

    def test_toDecimal_hi(self):
        output = self._run('print("hi".toDecimal())')
        assert output[-1] == "104,105"
