"""
Tests for string .toQuindecHashDelimited() method - join words with 15 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecHashDelimited_basic(self):
        output = self._run('print("hello world".toQuindecHashDelimited())')
        assert output[-1] == "hello###############world"

    def test_toQuindecHashDelimited_three(self):
        output = self._run('print("a b c".toQuindecHashDelimited())')
        assert output[-1] == "a###############b###############c"
