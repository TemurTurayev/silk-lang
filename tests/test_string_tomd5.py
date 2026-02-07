"""
Tests for string .toMd5() method - MD5 hash.
"""

from silk.interpreter import Interpreter


class TestStringToMd5:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMd5_hello(self):
        output = self._run('print("hello".toMd5())')
        assert output[-1] == "5d41402abc4b2a76b9719d911017c592"

    def test_toMd5_empty(self):
        output = self._run('print("".toMd5())')
        assert output[-1] == "d41d8cd98f00b204e9800998ecf8427e"
