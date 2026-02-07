"""
Tests for string .charCount() method - unique character count.
"""

from silk.interpreter import Interpreter


class TestStringCharCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_charCount_basic(self):
        output = self._run('print("hello".charCount())')
        assert output[-1] == "4"

    def test_charCount_all_unique(self):
        output = self._run('print("abc".charCount())')
        assert output[-1] == "3"
