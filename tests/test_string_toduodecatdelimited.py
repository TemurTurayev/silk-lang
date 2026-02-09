"""
Tests for string .toDuodecAtDelimited() method - split words by @@@@@@@@@@@@ (12 ats).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecAtDelimited_basic(self):
        output = self._run('print("hello world".toDuodecAtDelimited())')
        assert output[-1] == "hello@@@@@@@@@@@@world"

    def test_toDuodecAtDelimited_three(self):
        output = self._run('print("a b c".toDuodecAtDelimited())')
        assert output[-1] == "a@@@@@@@@@@@@b@@@@@@@@@@@@c"
