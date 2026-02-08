"""
Tests for string .toColumnar(cols) method - columnar transposition cipher.
"""

from silk.interpreter import Interpreter


class TestStringToColumnar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toColumnar_2cols(self):
        output = self._run('print("hello".toColumnar(2))')
        assert output[-1] == "hloel"

    def test_toColumnar_3cols(self):
        output = self._run('print("abcdef".toColumnar(3))')
        assert output[-1] == "adbecf"
