"""
Tests for string .isBalanced() method.
"""

from silk.interpreter import Interpreter


class TestStringIsBalanced:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isBalanced_true(self):
        output = self._run('print("(hello [world])".isBalanced())')
        assert output[-1] == "true"

    def test_isBalanced_false(self):
        output = self._run('print("(hello [world)".isBalanced())')
        assert output[-1] == "false"

    def test_isBalanced_empty(self):
        output = self._run('print("".isBalanced())')
        assert output[-1] == "true"
