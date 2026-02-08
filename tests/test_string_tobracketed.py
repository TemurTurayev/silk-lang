"""
Tests for string .toBracketed() method - wrap string in square brackets.
"""

from silk.interpreter import Interpreter


class TestStringToBracketed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBracketed_basic(self):
        output = self._run('print("hello".toBracketed())')
        assert output[-1] == "[hello]"

    def test_toBracketed_word(self):
        output = self._run('print("test".toBracketed())')
        assert output[-1] == "[test]"
