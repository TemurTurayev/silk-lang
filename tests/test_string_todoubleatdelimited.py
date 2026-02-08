"""
Tests for string .toDoubleAtDelimited() method - split words by @@.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleAtDelimited_basic(self):
        output = self._run('print("hello world".toDoubleAtDelimited())')
        assert output[-1] == "hello@@world"

    def test_toDoubleAtDelimited_three(self):
        output = self._run('print("a b c".toDoubleAtDelimited())')
        assert output[-1] == "a@@b@@c"
