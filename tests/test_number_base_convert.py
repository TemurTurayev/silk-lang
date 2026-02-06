"""
Tests for number .toBinary() and .toHex() methods.
"""

from silk.interpreter import Interpreter


class TestNumberBaseConvert:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBinary_basic(self):
        output = self._run('print(10.toBinary())')
        assert output[-1] == "1010"

    def test_toBinary_zero(self):
        output = self._run('print(0.toBinary())')
        assert output[-1] == "0"

    def test_toBinary_power(self):
        output = self._run('print(255.toBinary())')
        assert output[-1] == "11111111"

    def test_toHex_basic(self):
        output = self._run('print(255.toHex())')
        assert output[-1] == "ff"

    def test_toHex_zero(self):
        output = self._run('print(0.toHex())')
        assert output[-1] == "0"

    def test_toHex_large(self):
        output = self._run('print(4096.toHex())')
        assert output[-1] == "1000"
