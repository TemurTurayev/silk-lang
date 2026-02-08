"""
Tests for string .toHeaderCase() method - capitalized hyphen-separated.
"""

from silk.interpreter import Interpreter


class TestStringToHeaderCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHeaderCase_basic(self):
        output = self._run('print("hello world".toHeaderCase())')
        assert output[-1] == "Hello-World"

    def test_toHeaderCase_underscores(self):
        output = self._run('print("foo_bar_baz".toHeaderCase())')
        assert output[-1] == "Foo-Bar-Baz"
