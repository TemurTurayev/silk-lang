"""
Tests for string .toNonPlusDelimited() method - split words by +++++++++ (9 plus signs).
"""

from silk.interpreter import Interpreter


class TestStringToNonPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toNonPlusDelimited_basic(self):
        output = self._run('print("hello world".toNonPlusDelimited())')
        assert output[-1] == "hello+++++++++world"

    def test_toNonPlusDelimited_three(self):
        output = self._run('print("a b c".toNonPlusDelimited())')
        assert output[-1] == "a+++++++++b+++++++++c"
