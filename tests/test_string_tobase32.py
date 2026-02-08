"""
Tests for string .toBase32() method - base32 encoding.
"""

from silk.interpreter import Interpreter


class TestStringToBase32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBase32_hello(self):
        output = self._run('print("hello".toBase32())')
        assert output[-1] == "NBSWY3DP"

    def test_toBase32_empty(self):
        output = self._run('print("".toBase32())')
        assert output[-1] == ""
