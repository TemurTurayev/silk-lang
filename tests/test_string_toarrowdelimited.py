"""
Tests for string .toArrowDelimited() method - split words by arrow (->).
"""

from silk.interpreter import Interpreter


class TestStringToArrowDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toArrowDelimited_basic(self):
        output = self._run('print("hello world".toArrowDelimited())')
        assert output[-1] == "hello->world"

    def test_toArrowDelimited_three(self):
        output = self._run('print("a b c".toArrowDelimited())')
        assert output[-1] == "a->b->c"
