"""
Tests for string .toAtbash() method - Atbash cipher (a→z, b→y, etc).
"""

from silk.interpreter import Interpreter


class TestStringToAtbash:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAtbash_hello(self):
        output = self._run('print("hello".toAtbash())')
        assert output[-1] == "svool"

    def test_toAtbash_abc(self):
        output = self._run('print("abc".toAtbash())')
        assert output[-1] == "zyx"
