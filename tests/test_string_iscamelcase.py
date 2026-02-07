"""
Tests for string .isCamelCase() method.
"""

from silk.interpreter import Interpreter


class TestStringIsCamelCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isCamelCase_true(self):
        output = self._run('print("myVarName".isCamelCase())')
        assert output[-1] == "true"

    def test_isCamelCase_false(self):
        output = self._run('print("MyVarName".isCamelCase())')
        assert output[-1] == "false"

    def test_isCamelCase_snake(self):
        output = self._run('print("my_var".isCamelCase())')
        assert output[-1] == "false"
