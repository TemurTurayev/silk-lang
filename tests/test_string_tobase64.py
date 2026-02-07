"""
Tests for string .toBase64() method.
"""

from silk.interpreter import Interpreter


class TestStringToBase64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBase64_basic(self):
        output = self._run('print("hello".toBase64())')
        assert output[-1] == "aGVsbG8="

    def test_toBase64_sentence(self):
        output = self._run('print("Hello World".toBase64())')
        assert output[-1] == "SGVsbG8gV29ybGQ="
