"""
Tests for string .toA1Z26() method - A1Z26 cipher (a=1, b=2, ..., z=26).
"""

from silk.interpreter import Interpreter


class TestStringToA1Z26:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toA1Z26_abc(self):
        output = self._run('print("abc".toA1Z26())')
        assert output[-1] == "1-2-3"

    def test_toA1Z26_hello(self):
        output = self._run('print("hello".toA1Z26())')
        assert output[-1] == "8-5-12-12-15"
