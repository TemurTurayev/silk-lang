"""
Tests for number .toChar() method.
"""

from silk.interpreter import Interpreter


class TestNumberToChar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toChar_A(self):
        output = self._run('print(65.toChar())')
        assert output[-1] == "A"

    def test_toChar_a(self):
        output = self._run('print(97.toChar())')
        assert output[-1] == "a"

    def test_toChar_space(self):
        output = self._run('print(32.toChar())')
        assert output[-1] == " "
