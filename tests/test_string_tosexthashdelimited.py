"""
Tests for string .toSextHashDelimited() method - split words by ######.
"""

from silk.interpreter import Interpreter


class TestStringToSextHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextHashDelimited_basic(self):
        output = self._run('print("hello world".toSextHashDelimited())')
        assert output[-1] == "hello######world"

    def test_toSextHashDelimited_three(self):
        output = self._run('print("a b c".toSextHashDelimited())')
        assert output[-1] == "a######b######c"
