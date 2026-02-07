"""
Tests for string .toDotCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToDotCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDotCase_from_camel(self):
        output = self._run('print("myVarName".toDotCase())')
        assert output[-1] == "my.var.name"

    def test_toDotCase_from_snake(self):
        output = self._run('print("foo_bar_baz".toDotCase())')
        assert output[-1] == "foo.bar.baz"

    def test_toDotCase_from_spaces(self):
        output = self._run('print("hello world".toDotCase())')
        assert output[-1] == "hello.world"
