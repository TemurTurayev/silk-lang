"""
Tests for string .isHexColor() method.
"""

from silk.interpreter import Interpreter


class TestStringIsHexColor:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHexColor_six_digit(self):
        output = self._run('print("#FF5733".isHexColor())')
        assert output[-1] == "true"

    def test_isHexColor_three_digit(self):
        output = self._run('print("#abc".isHexColor())')
        assert output[-1] == "true"

    def test_isHexColor_invalid(self):
        output = self._run('print("hello".isHexColor())')
        assert output[-1] == "false"

    def test_isHexColor_no_hash(self):
        output = self._run('print("FF5733".isHexColor())')
        assert output[-1] == "false"
