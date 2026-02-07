"""
Tests for string .toSnakeCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToSnakeCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSnakeCase_basic(self):
        output = self._run('print("hello world".toSnakeCase())')
        assert output[-1] == "hello_world"

    def test_toSnakeCase_camel(self):
        output = self._run('print("helloWorld".toSnakeCase())')
        assert output[-1] == "hello_world"
