"""
Tests for string .toQuintHashDelimited() method - split words by #####.
"""

from silk.interpreter import Interpreter


class TestStringToQuintHashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintHashDelimited_basic(self):
        output = self._run('print("hello world".toQuintHashDelimited())')
        assert output[-1] == "hello#####world"

    def test_toQuintHashDelimited_three(self):
        output = self._run('print("a b c".toQuintHashDelimited())')
        assert output[-1] == "a#####b#####c"
