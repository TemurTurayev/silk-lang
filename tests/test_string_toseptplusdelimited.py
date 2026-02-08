"""
Tests for string .toSeptPlusDelimited() method - split words by +++++++.
"""

from silk.interpreter import Interpreter


class TestStringToSeptPlusDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptPlusDelimited_basic(self):
        output = self._run('print("hello world".toSeptPlusDelimited())')
        assert output[-1] == "hello+++++++world"

    def test_toSeptPlusDelimited_three(self):
        output = self._run('print("a b c".toSeptPlusDelimited())')
        assert output[-1] == "a+++++++b+++++++c"
