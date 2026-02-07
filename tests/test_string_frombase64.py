"""
Tests for string .fromBase64() method.
"""

from silk.interpreter import Interpreter


class TestStringFromBase64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fromBase64_basic(self):
        output = self._run('print("aGVsbG8=".fromBase64())')
        assert output[-1] == "hello"

    def test_fromBase64_sentence(self):
        output = self._run('print("SGVsbG8gV29ybGQ=".fromBase64())')
        assert output[-1] == "Hello World"
