"""
Tests for string .toSextPlusDelimited() method - split words by ++++++.
"""

from silk.interpreter import Interpreter


class TestStringToSextPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextPlusDelimited_basic(self):
        output = self._run('print("hello world".toSextPlusDelimited())')
        assert output[-1] == "hello++++++world"

    def test_toSextPlusDelimited_three(self):
        output = self._run('print("a b c".toSextPlusDelimited())')
        assert output[-1] == "a++++++b++++++c"
