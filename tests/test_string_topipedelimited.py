"""
Tests for string .toPipeDelimited() method - split words by pipe.
"""

from silk.interpreter import Interpreter


class TestStringToPipeDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPipeDelimited_basic(self):
        output = self._run('print("hello world".toPipeDelimited())')
        assert output[-1] == "hello|world"

    def test_toPipeDelimited_three(self):
        output = self._run('print("a b c".toPipeDelimited())')
        assert output[-1] == "a|b|c"
