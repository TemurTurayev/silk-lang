"""
Tests for string .toSedecHashDelimited() method - join words with 16 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToSedecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSedecHashDelimited_basic(self):
        output = self._run('print("hello world".toSedecHashDelimited())')
        assert output[-1] == "hello################world"

    def test_toSedecHashDelimited_three(self):
        output = self._run('print("a b c".toSedecHashDelimited())')
        assert output[-1] == "a################b################c"
