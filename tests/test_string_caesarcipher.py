"""
Tests for string .caesarCipher(n) method - Caesar cipher shift.
"""

from silk.interpreter import Interpreter


class TestStringCaesarCipher:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_caesarCipher_3(self):
        output = self._run('print("hello".caesarCipher(3))')
        assert output[-1] == "khoor"

    def test_caesarCipher_neg(self):
        output = self._run('print("khoor".caesarCipher(-3))')
        assert output[-1] == "hello"
