"""
Tests for string .toTitleSlug() method.
"""

from silk.interpreter import Interpreter


class TestStringToTitleSlug:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTitleSlug_basic(self):
        output = self._run('print("Hello World!".toTitleSlug())')
        assert output[-1] == "hello-world"

    def test_toTitleSlug_special(self):
        output = self._run('print("My Article: A Story".toTitleSlug())')
        assert output[-1] == "my-article-a-story"

    def test_toTitleSlug_spaces(self):
        output = self._run('print("  extra  spaces  ".toTitleSlug())')
        assert output[-1] == "extra-spaces"
