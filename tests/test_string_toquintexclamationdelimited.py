"""
Tests for string .toQuintExclamationDelimited() method - split words by !!!!!.
"""

from silk.interpreter import Interpreter


class TestStringToQuintExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuintExclamationDelimited_basic(self):
        output = self._run('print("hello world".toQuintExclamationDelimited())')
        assert output[-1] == "hello!!!!!world"

    def test_toQuintExclamationDelimited_three(self):
        output = self._run('print("a b c".toQuintExclamationDelimited())')
        assert output[-1] == "a!!!!!b!!!!!c"
