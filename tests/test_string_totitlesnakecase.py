"""
Tests for string .toTitleSnakeCase() method - Title_Snake_Case conversion.
"""

from silk.interpreter import Interpreter


class TestStringToTitleSnakeCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTitleSnakeCase_basic(self):
        output = self._run('print("hello world".toTitleSnakeCase())')
        assert output[-1] == "Hello_World"

    def test_toTitleSnakeCase_single(self):
        output = self._run('print("foo".toTitleSnakeCase())')
        assert output[-1] == "Foo"
