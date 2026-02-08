"""
Tests for string .toDoubleHashDelimited() method - split words by ##.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleHashDelimited_basic(self):
        output = self._run('print("hello world".toDoubleHashDelimited())')
        assert output[-1] == "hello##world"

    def test_toDoubleHashDelimited_three(self):
        output = self._run('print("a b c".toDoubleHashDelimited())')
        assert output[-1] == "a##b##c"
