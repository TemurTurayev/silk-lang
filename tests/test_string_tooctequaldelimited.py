"""
Tests for string .toOctEqualDelimited() method - split words by ========.
"""

from silk.interpreter import Interpreter


class TestStringToOctEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctEqualDelimited_basic(self):
        output = self._run('print("hello world".toOctEqualDelimited())')
        assert output[-1] == "hello========world"

    def test_toOctEqualDelimited_three(self):
        output = self._run('print("a b c".toOctEqualDelimited())')
        assert output[-1] == "a========b========c"
