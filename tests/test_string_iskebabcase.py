"""
Tests for string .isKebabCase() method.
"""

from silk.interpreter import Interpreter


class TestStringIsKebabCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isKebabCase_true(self):
        output = self._run('print("my-var-name".isKebabCase())')
        assert output[-1] == "true"

    def test_isKebabCase_false(self):
        output = self._run('print("myVarName".isKebabCase())')
        assert output[-1] == "false"

    def test_isKebabCase_simple(self):
        output = self._run('print("hello".isKebabCase())')
        assert output[-1] == "true"
