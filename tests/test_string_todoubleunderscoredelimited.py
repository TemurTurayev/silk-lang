"""
Tests for string .toDoubleUnderscoreDelimited() method - split words by __.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toDoubleUnderscoreDelimited())')
        assert output[-1] == "hello__world"

    def test_toDoubleUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toDoubleUnderscoreDelimited())')
        assert output[-1] == "a__b__c"
