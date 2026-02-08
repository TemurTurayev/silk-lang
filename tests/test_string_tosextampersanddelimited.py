"""
Tests for string .toSextAmpersandDelimited() method - split words by &&&&&&.
"""

from silk.interpreter import Interpreter


class TestStringToSextAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toSextAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&world"

    def test_toSextAmpersandDelimited_three(self):
        output = self._run('print("a b c".toSextAmpersandDelimited())')
        assert output[-1] == "a&&&&&&b&&&&&&c"
