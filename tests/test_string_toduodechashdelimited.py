"""
Tests for string .toDuodecHashDelimited() method - split words by ############ (12 hashes).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecHashDelimited_basic(self):
        output = self._run('print("hello world".toDuodecHashDelimited())')
        assert output[-1] == "hello############world"

    def test_toDuodecHashDelimited_three(self):
        output = self._run('print("a b c".toDuodecHashDelimited())')
        assert output[-1] == "a############b############c"
