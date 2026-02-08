"""
Tests for string .toDoubleArrowDelimited() method - split words by =>.
"""

from silk.interpreter import Interpreter


class TestStringToDoubleArrowDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDoubleArrowDelimited_basic(self):
        output = self._run('print("hello world".toDoubleArrowDelimited())')
        assert output[-1] == "hello=>world"

    def test_toDoubleArrowDelimited_three(self):
        output = self._run('print("a b c".toDoubleArrowDelimited())')
        assert output[-1] == "a=>b=>c"
