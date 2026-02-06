"""
Tests for string .caesar(shift) method.
"""

from silk.interpreter import Interpreter


class TestStringCaesar:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_caesar_basic(self):
        output = self._run('print("abc".caesar(3))')
        assert output[-1] == "def"

    def test_caesar_wrap(self):
        output = self._run('print("xyz".caesar(3))')
        assert output[-1] == "abc"

    def test_caesar_negative(self):
        output = self._run('print("def".caesar(-3))')
        assert output[-1] == "abc"

    def test_caesar_preserves_case(self):
        output = self._run('print("Hello World!".caesar(13))')
        assert output[-1] == "Uryyb Jbeyq!"
