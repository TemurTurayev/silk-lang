"""
Tests for string .toConstantCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToConstantCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toConstantCase_from_camel(self):
        output = self._run('print("myVarName".toConstantCase())')
        assert output[-1] == "MY_VAR_NAME"

    def test_toConstantCase_from_kebab(self):
        output = self._run('print("foo-bar".toConstantCase())')
        assert output[-1] == "FOO_BAR"

    def test_toConstantCase_from_spaces(self):
        output = self._run('print("hello world".toConstantCase())')
        assert output[-1] == "HELLO_WORLD"
