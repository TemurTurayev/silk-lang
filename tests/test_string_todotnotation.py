"""
Tests for string .toDotNotation() method - dot.separated format.
"""

from silk.interpreter import Interpreter


class TestStringToDotNotation:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDotNotation_basic(self):
        output = self._run('print("hello world".toDotNotation())')
        assert output[-1] == "hello.world"

    def test_toDotNotation_underscore(self):
        output = self._run('print("foo_bar_baz".toDotNotation())')
        assert output[-1] == "foo.bar.baz"
