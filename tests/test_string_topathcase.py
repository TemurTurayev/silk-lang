"""
Tests for string .toPathCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToPathCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPathCase_from_camel(self):
        output = self._run('print("myVarName".toPathCase())')
        assert output[-1] == "my/var/name"

    def test_toPathCase_from_snake(self):
        output = self._run('print("foo_bar".toPathCase())')
        assert output[-1] == "foo/bar"

    def test_toPathCase_from_spaces(self):
        output = self._run('print("hello world".toPathCase())')
        assert output[-1] == "hello/world"
