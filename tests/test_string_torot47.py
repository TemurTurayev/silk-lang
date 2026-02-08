"""
Tests for string .toROT47() method - ROT47 cipher.
"""

from silk.interpreter import Interpreter


class TestStringToROT47:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toROT47_hello(self):
        output = self._run('print("Hello".toROT47())')
        assert output[-1] == "w6==@"

    def test_toROT47_number(self):
        output = self._run('print("123".toROT47())')
        assert output[-1] == "`ab"
