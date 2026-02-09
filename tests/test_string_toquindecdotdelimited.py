"""
Tests for string .toQuindecDotDelimited() method - join words with 15 dots.
"""

from silk.interpreter import Interpreter


class TestStringToQuindecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuindecDotDelimited_basic(self):
        output = self._run('print("hello world".toQuindecDotDelimited())')
        assert output[-1] == "hello...............world"

    def test_toQuindecDotDelimited_three(self):
        output = self._run('print("a b c".toQuindecDotDelimited())')
        assert output[-1] == "a...............b...............c"
