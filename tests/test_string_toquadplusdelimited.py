"""
Tests for string .toQuadPlusDelimited() method - split words by ++++.
"""

from silk.interpreter import Interpreter


class TestStringToQuadPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadPlusDelimited_basic(self):
        output = self._run('print("hello world".toQuadPlusDelimited())')
        assert output[-1] == "hello++++world"

    def test_toQuadPlusDelimited_three(self):
        output = self._run('print("a b c".toQuadPlusDelimited())')
        assert output[-1] == "a++++b++++c"
