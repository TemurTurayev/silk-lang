"""
Tests for string .isAscii() method.
"""

from silk.interpreter import Interpreter


class TestStringIsAscii:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAscii_true(self):
        output = self._run('print("hello".isAscii())')
        assert output[-1] == "true"

    def test_isAscii_false(self):
        output = self._run('print("caf\u00e9".isAscii())')
        assert output[-1] == "false"

    def test_isAscii_empty(self):
        output = self._run('print("".isAscii())')
        assert output[-1] == "true"
