"""
Tests for string .toUnvigintiCommaDelimited() method - join words with 21 commas.
"""

from silk.interpreter import Interpreter


class TestStringToUnvigintiCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUnvigintiCommaDelimited_basic(self):
        output = self._run('print("hello world".toUnvigintiCommaDelimited())')
        assert output[-1] == "hello" + "," * 21 + "world"

    def test_toUnvigintiCommaDelimited_multi(self):
        output = self._run('print("a b c".toUnvigintiCommaDelimited())')
        assert output[-1] == "a" + "," * 21 + "b" + "," * 21 + "c"
