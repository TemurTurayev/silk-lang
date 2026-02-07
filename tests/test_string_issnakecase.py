"""
Tests for string .isSnakeCase() method.
"""

from silk.interpreter import Interpreter


class TestStringIsSnakeCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSnakeCase_true(self):
        output = self._run('print("my_var_name".isSnakeCase())')
        assert output[-1] == "true"

    def test_isSnakeCase_false(self):
        output = self._run('print("myVarName".isSnakeCase())')
        assert output[-1] == "false"

    def test_isSnakeCase_simple(self):
        output = self._run('print("hello".isSnakeCase())')
        assert output[-1] == "true"
