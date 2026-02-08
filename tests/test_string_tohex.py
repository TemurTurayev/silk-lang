"""
Tests for string .toHex() method - hex encode string bytes.
"""

from silk.interpreter import Interpreter


class TestStringToHex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHex_hello(self):
        output = self._run('print("hello".toHex())')
        assert output[-1] == "68656c6c6f"

    def test_toHex_empty(self):
        output = self._run('print("".toHex())')
        assert output[-1] == ""
