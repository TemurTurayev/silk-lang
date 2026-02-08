"""
Tests for string .toDoubleExclamationDelimited() method - split words by !!.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleExclamationDelimited_basic(self):
        output = self._run('print("hello world".toDoubleExclamationDelimited())')
        assert output[-1] == "hello!!world"

    def test_toDoubleExclamationDelimited_three(self):
        output = self._run('print("a b c".toDoubleExclamationDelimited())')
        assert output[-1] == "a!!b!!c"
