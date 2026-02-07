"""
Tests for string .wordWrap(width) method.
"""

from silk.interpreter import Interpreter


class TestStringWordWrap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_wordWrap_basic(self):
        output = self._run('print("hello world foo bar".wordWrap(10))')
        assert output[-1] == "hello\nworld foo\nbar"

    def test_wordWrap_single_word(self):
        output = self._run('print("hello".wordWrap(10))')
        assert output[-1] == "hello"

    def test_wordWrap_exact_width(self):
        output = self._run('print("hi there".wordWrap(8))')
        assert output[-1] == "hi there"
