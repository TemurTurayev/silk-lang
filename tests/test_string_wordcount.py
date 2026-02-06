"""
Tests for string .wordCount() method.
"""

from silk.interpreter import Interpreter


class TestStringWordCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_wordCount_basic(self):
        output = self._run('print("hello world foo".wordCount())')
        assert output[-1] == "3"

    def test_wordCount_single(self):
        output = self._run('print("hello".wordCount())')
        assert output[-1] == "1"

    def test_wordCount_empty(self):
        output = self._run('print("".wordCount())')
        assert output[-1] == "0"
