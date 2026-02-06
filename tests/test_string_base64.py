"""
Tests for string .encodeBase64() and .decodeBase64() methods.
"""

from silk.interpreter import Interpreter


class TestStringBase64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_encodeBase64(self):
        output = self._run('print("hello".encodeBase64())')
        assert output[-1] == "aGVsbG8="

    def test_decodeBase64(self):
        output = self._run('print("aGVsbG8=".decodeBase64())')
        assert output[-1] == "hello"

    def test_roundtrip(self):
        output = self._run('print("silk lang".encodeBase64().decodeBase64())')
        assert output[-1] == "silk lang"
