"""
Tests for string .toCRC32() method - CRC32 checksum.
"""

from silk.interpreter import Interpreter


class TestStringToCRC32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCRC32_hello(self):
        output = self._run('print("hello".toCRC32())')
        assert output[-1] == "3610a686"

    def test_toCRC32_empty(self):
        output = self._run('print("".toCRC32())')
        assert output[-1] == "00000000"
