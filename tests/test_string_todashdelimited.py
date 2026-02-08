"""
Tests for string .toDashDelimited() method - split words by dash.
"""

from silk.interpreter import Interpreter


class TestStringToDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDashDelimited_basic(self):
        output = self._run('print("hello world".toDashDelimited())')
        assert output[-1] == "hello-world"

    def test_toDashDelimited_three(self):
        output = self._run('print("a b c".toDashDelimited())')
        assert output[-1] == "a-b-c"
