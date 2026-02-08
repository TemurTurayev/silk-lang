"""
Tests for string .toAngleBracketed() method - wrap string in angle brackets.
"""

from silk.interpreter import Interpreter


class TestStringToAngleBracketed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAngleBracketed_basic(self):
        output = self._run('print("hello".toAngleBracketed())')
        assert output[-1] == "<hello>"

    def test_toAngleBracketed_word(self):
        output = self._run('print("test".toAngleBracketed())')
        assert output[-1] == "<test>"
