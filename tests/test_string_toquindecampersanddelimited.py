"""
Tests for string .toQuindecAmpersandDelimited() method - join words with 15 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toQuindecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&&&&&&world"

    def test_toQuindecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toQuindecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&&&&&&b&&&&&&&&&&&&&&&c"
