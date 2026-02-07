"""
Tests for string .toSentenceCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToSentenceCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSentenceCase_basic(self):
        output = self._run('print("hello world".toSentenceCase())')
        assert output[-1] == "Hello world"

    def test_toSentenceCase_from_upper(self):
        output = self._run('print("HELLO WORLD".toSentenceCase())')
        assert output[-1] == "Hello world"

    def test_toSentenceCase_single(self):
        output = self._run('print("hello".toSentenceCase())')
        assert output[-1] == "Hello"
