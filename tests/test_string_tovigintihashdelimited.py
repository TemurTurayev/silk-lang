"""
Tests for string .toVigintiHashDelimited() method - join words with 20 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiHashDelimited_basic(self):
        output = self._run('print("hello world".toVigintiHashDelimited())')
        assert output[-1] == "hello####################world"

    def test_toVigintiHashDelimited_multi(self):
        output = self._run('print("a b c".toVigintiHashDelimited())')
        assert output[-1] == "a####################b####################c"
