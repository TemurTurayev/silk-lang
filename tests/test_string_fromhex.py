"""
Tests for string .fromHex() method - decode hex-encoded string.
"""

from silk.interpreter import Interpreter


class TestStringFromHex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fromHex_hello(self):
        output = self._run('print("68656c6c6f".fromHex())')
        assert output[-1] == "hello"

    def test_fromHex_empty(self):
        output = self._run('print("".fromHex())')
        assert output[-1] == ""
