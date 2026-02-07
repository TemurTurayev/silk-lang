"""
Tests for string .toKebabCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToKebabCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toKebabCase_basic(self):
        output = self._run('print("hello world".toKebabCase())')
        assert output[-1] == "hello-world"

    def test_toKebabCase_camel(self):
        output = self._run('print("helloWorld".toKebabCase())')
        assert output[-1] == "hello-world"
