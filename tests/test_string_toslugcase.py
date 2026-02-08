"""
Tests for string .toSlugCase() method - lowercase hyphen-separated.
"""

from silk.interpreter import Interpreter


class TestStringToSlugCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSlugCase_basic(self):
        output = self._run('print("Hello World".toSlugCase())')
        assert output[-1] == "hello-world"

    def test_toSlugCase_underscores(self):
        output = self._run('print("foo_bar_baz".toSlugCase())')
        assert output[-1] == "foo-bar-baz"
