"""
Tests for string .toSha256() method - SHA-256 hash.
"""

from silk.interpreter import Interpreter


class TestStringToSha256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSha256_hello(self):
        output = self._run('print("hello".toSha256())')
        assert output[-1] == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

    def test_toSha256_empty(self):
        output = self._run('print("".toSha256())')
        assert output[-1] == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
