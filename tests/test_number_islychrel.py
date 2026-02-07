"""
Tests for number .isLychrel(maxIter) method.
"""

from silk.interpreter import Interpreter


class TestNumberIsLychrel:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isLychrel_false(self):
        output = self._run('print(56.isLychrel(50))')
        assert output[-1] == "false"

    def test_isLychrel_196(self):
        output = self._run('print(196.isLychrel(50))')
        assert output[-1] == "true"

    def test_isLychrel_palindrome(self):
        output = self._run('print(11.isLychrel(50))')
        assert output[-1] == "false"
