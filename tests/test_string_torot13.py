"""
Tests for string .toROT13() method - ROT13 cipher.
"""

from silk.interpreter import Interpreter


class TestStringToROT13:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toROT13_hello(self):
        output = self._run('print("hello".toROT13())')
        assert output[-1] == "uryyb"

    def test_toROT13_double(self):
        output = self._run('print("uryyb".toROT13())')
        assert output[-1] == "hello"
