"""
Tests for string .toDuovigintiHashDelimited() method - join words with 22 hash chars.
"""

from silk.interpreter import Interpreter


class TestStringToDuovigintiHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuovigintiHashDelimited_basic(self):
        output = self._run('print("hello world".toDuovigintiHashDelimited())')
        assert output[-1] == "hello" + "#" * 22 + "world"

    def test_toDuovigintiHashDelimited_multi(self):
        output = self._run('print("a b c".toDuovigintiHashDelimited())')
        assert output[-1] == "a" + "#" * 22 + "b" + "#" * 22 + "c"
