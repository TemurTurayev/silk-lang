"""
Tests for string .toOctHashDelimited() method - split words by ########.
"""

from silk.interpreter import Interpreter


class TestStringToOctHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctHashDelimited_basic(self):
        output = self._run('print("hello world".toOctHashDelimited())')
        assert output[-1] == "hello########world"

    def test_toOctHashDelimited_three(self):
        output = self._run('print("a b c".toOctHashDelimited())')
        assert output[-1] == "a########b########c"
