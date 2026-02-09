"""
Tests for string .toVigintiEqualDelimited() method - join words with 20 equals.
"""

from silk.interpreter import Interpreter


class TestStringToVigintiEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toVigintiEqualDelimited_basic(self):
        output = self._run('print("hello world".toVigintiEqualDelimited())')
        assert output[-1] == "hello====================world"

    def test_toVigintiEqualDelimited_multi(self):
        output = self._run('print("a b c".toVigintiEqualDelimited())')
        assert output[-1] == "a====================b====================c"
