"""
Tests for string .isUpperCamelCase() method.
"""

from silk.interpreter import Interpreter


class TestStringIsUpperCamelCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isUpperCamelCase_true(self):
        output = self._run('print("MyVarName".isUpperCamelCase())')
        assert output[-1] == "true"

    def test_isUpperCamelCase_false(self):
        output = self._run('print("myVarName".isUpperCamelCase())')
        assert output[-1] == "false"

    def test_isUpperCamelCase_single(self):
        output = self._run('print("Hello".isUpperCamelCase())')
        assert output[-1] == "true"
