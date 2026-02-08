"""
Tests for string .toTripleAtDelimited() method - split words by @@@.
"""

from silk.interpreter import Interpreter


class TestStringToTripleAtDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleAtDelimited_basic(self):
        output = self._run('print("hello world".toTripleAtDelimited())')
        assert output[-1] == "hello@@@world"

    def test_toTripleAtDelimited_three(self):
        output = self._run('print("a b c".toTripleAtDelimited())')
        assert output[-1] == "a@@@b@@@c"
