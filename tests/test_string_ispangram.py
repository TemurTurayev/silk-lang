"""
Tests for string .isPangram() method.
"""

from silk.interpreter import Interpreter


class TestStringIsPangram:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPangram_true(self):
        output = self._run('print("The quick brown fox jumps over the lazy dog".isPangram())')
        assert output[-1] == "true"

    def test_isPangram_false(self):
        output = self._run('print("Hello world".isPangram())')
        assert output[-1] == "false"

    def test_isPangram_empty(self):
        output = self._run('print("".isPangram())')
        assert output[-1] == "false"
