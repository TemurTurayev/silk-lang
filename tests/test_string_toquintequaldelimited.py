"""
Tests for string .toQuintEqualDelimited() method - split words by =====.
"""

from silk.interpreter import Interpreter


class TestStringToQuintEqualDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintEqualDelimited_basic(self):
        output = self._run('print("hello world".toQuintEqualDelimited())')
        assert output[-1] == "hello=====world"

    def test_toQuintEqualDelimited_three(self):
        output = self._run('print("a b c".toQuintEqualDelimited())')
        assert output[-1] == "a=====b=====c"
