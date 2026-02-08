"""
Tests for string .toWordBoundary() method - split on word boundaries (camelCase, snake_case, etc).
"""

from silk.interpreter import Interpreter


class TestStringToWordBoundary:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWordBoundary_camel(self):
        output = self._run('print("helloWorld".toWordBoundary())')
        assert output[-1] == "[hello, World]"

    def test_toWordBoundary_snake(self):
        output = self._run('print("hello_world".toWordBoundary())')
        assert output[-1] == "[hello, world]"
