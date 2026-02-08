"""
Tests for string .toOctAmpersandDelimited() method - split words by &&&&&&&&.
"""

from silk.interpreter import Interpreter


class TestStringToOctAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toOctAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toOctAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&world"

    def test_toOctAmpersandDelimited_three(self):
        output = self._run('print("a b c".toOctAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&b&&&&&&&&c"
