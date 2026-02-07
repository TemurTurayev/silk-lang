"""
Tests for string .toCamelCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToCamelCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCamelCase_basic(self):
        output = self._run('print("hello world".toCamelCase())')
        assert output[-1] == "helloWorld"

    def test_toCamelCase_snake(self):
        output = self._run('print("hello_world".toCamelCase())')
        assert output[-1] == "helloWorld"
