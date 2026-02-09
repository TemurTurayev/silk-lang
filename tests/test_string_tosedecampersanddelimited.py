"""
Tests for string .toSedecAmpersandDelimited() method - join words with 16 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToSedecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toSedecAmpersandDelimited())')
        assert output[-1] == "hello" + "&" * 16 + "world"

    def test_toSedecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toSedecAmpersandDelimited())')
        assert output[-1] == "a" + "&" * 16 + "b" + "&" * 16 + "c"
