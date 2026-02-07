"""
Tests for string .toSlug() method.
"""

from silk.interpreter import Interpreter


class TestStringToSlug:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSlug_basic(self):
        output = self._run('print("Hello World".toSlug())')
        assert output[-1] == "hello-world"

    def test_toSlug_special_chars(self):
        output = self._run('print("Hello, World! 123".toSlug())')
        assert output[-1] == "hello-world-123"
