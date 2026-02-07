"""
Tests for string .sizeInBytes() method.
"""

from silk.interpreter import Interpreter


class TestStringSizeInBytes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sizeInBytes_ascii(self):
        output = self._run('print("hello".sizeInBytes())')
        assert output[-1] == "5"

    def test_sizeInBytes_empty(self):
        output = self._run('print("".sizeInBytes())')
        assert output[-1] == "0"
