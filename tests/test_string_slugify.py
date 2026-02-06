"""
Tests for string .slugify() method.
"""

from silk.interpreter import Interpreter


class TestStringSlugify:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_slugify_basic(self):
        output = self._run('print("Hello World".slugify())')
        assert output[-1] == "hello-world"

    def test_slugify_special_chars(self):
        output = self._run('print("Hello, World! How are you?".slugify())')
        assert output[-1] == "hello-world-how-are-you"

    def test_slugify_extra_spaces(self):
        output = self._run('print("  foo   bar  baz  ".slugify())')
        assert output[-1] == "foo-bar-baz"
