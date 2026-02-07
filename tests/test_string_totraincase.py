"""
Tests for string .toTrainCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToTrainCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTrainCase_from_camel(self):
        output = self._run('print("myVarName".toTrainCase())')
        assert output[-1] == "My-Var-Name"

    def test_toTrainCase_from_snake(self):
        output = self._run('print("foo_bar".toTrainCase())')
        assert output[-1] == "Foo-Bar"

    def test_toTrainCase_from_spaces(self):
        output = self._run('print("hello world".toTrainCase())')
        assert output[-1] == "Hello-World"
