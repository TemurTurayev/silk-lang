"""
Tests for string .toSedecStarDelimited() method - join words with 16 stars.
"""

from silk.interpreter import Interpreter


class TestStringToSedecStarDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecStarDelimited_basic(self):
        output = self._run('print("hello world".toSedecStarDelimited())')
        assert output[-1] == "hello****************world"

    def test_toSedecStarDelimited_three(self):
        output = self._run('print("a b c".toSedecStarDelimited())')
        assert output[-1] == "a****************b****************c"
