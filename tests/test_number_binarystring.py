"""
Tests for number .toBinaryString(width) method.
"""

from silk.interpreter import Interpreter


class TestNumberToBinaryString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBinaryString_8bit(self):
        output = self._run('print(5.toBinaryString(8))')
        assert output[-1] == "00000101"

    def test_toBinaryString_4bit(self):
        output = self._run('print(10.toBinaryString(4))')
        assert output[-1] == "1010"

    def test_toBinaryString_default(self):
        output = self._run('print(255.toBinaryString(8))')
        assert output[-1] == "11111111"
