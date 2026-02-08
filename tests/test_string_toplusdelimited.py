"""
Tests for string .toPlusDelimited() method - split words by plus sign.
"""

from silk.interpreter import Interpreter


class TestStringToPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPlusDelimited_basic(self):
        output = self._run('print("hello world".toPlusDelimited())')
        assert output[-1] == "hello+world"

    def test_toPlusDelimited_three(self):
        output = self._run('print("a b c".toPlusDelimited())')
        assert output[-1] == "a+b+c"
