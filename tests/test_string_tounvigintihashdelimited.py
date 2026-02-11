"""
Tests for string .toUnvigintiHashDelimited() method - join words with 21 hashes.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiHashDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiHashDelimited())')
        assert output[-1] == "hello" + "#" * 21 + "world"

    def test_toUnvigintiHashDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiHashDelimited())')
        assert output[-1] == "a" + "#" * 21 + "b" + "#" * 21 + "c"
