"""
Tests for string .toVigintiCommaDelimited() method - join words with 20 commas.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiCommaDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiCommaDelimited_basic(self):
        output = self._run('print("hello world".toVigintiCommaDelimited())')
        assert output[-1] == "hello" + "," * 20 + "world"

    def test_toVigintiCommaDelimited_multi(self):
        output = self._run('print("a b c".toVigintiCommaDelimited())')
        assert output[-1] == "a" + "," * 20 + "b" + "," * 20 + "c"
