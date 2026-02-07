"""
Tests for string .isCreditCard() method (Luhn check).
"""

from silk.interpreter import Interpreter


class TestStringIsCreditCard:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCreditCard_valid(self):
        output = self._run('print("4532015112830366".isCreditCard())')
        assert output[-1] == "true"

    def test_isCreditCard_invalid(self):
        output = self._run('print("1234567890123456".isCreditCard())')
        assert output[-1] == "false"
