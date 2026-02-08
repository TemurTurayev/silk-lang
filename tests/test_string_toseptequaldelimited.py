"""
Tests for string .toSeptEqualDelimited() method - split words by =======.
"""

from silk.interpreter import Interpreter


class TestStringToSeptEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptEqualDelimited_basic(self):
        output = self._run('print("hello world".toSeptEqualDelimited())')
        assert output[-1] == "hello=======world"

    def test_toSeptEqualDelimited_three(self):
        output = self._run('print("a b c".toSeptEqualDelimited())')
        assert output[-1] == "a=======b=======c"
