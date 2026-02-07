"""
Tests for string .toPascalCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToPascalCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPascalCase_from_snake(self):
        output = self._run('print("hello_world".toPascalCase())')
        assert output[-1] == "HelloWorld"

    def test_toPascalCase_from_kebab(self):
        output = self._run('print("foo-bar-baz".toPascalCase())')
        assert output[-1] == "FooBarBaz"

    def test_toPascalCase_from_spaces(self):
        output = self._run('print("my variable name".toPascalCase())')
        assert output[-1] == "MyVariableName"
