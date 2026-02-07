"""
Tests for string .isHex() method.
"""

from silk.interpreter import Interpreter


class TestStringIsHex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHex_true(self):
        output = self._run('print("1a2b3c".isHex())')
        assert output[-1] == "true"

    def test_isHex_false(self):
        output = self._run('print("xyz".isHex())')
        assert output[-1] == "false"

    def test_isHex_empty(self):
        output = self._run('print("".isHex())')
        assert output[-1] == "false"
