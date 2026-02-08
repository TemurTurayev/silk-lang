"""
Tests for string .toSqueeze() method - remove consecutive duplicate chars.
"""

from silk.interpreter import Interpreter


class TestStringToSqueeze:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSqueeze_basic(self):
        output = self._run('print("aabbcc".toSqueeze())')
        assert output[-1] == "abc"

    def test_toSqueeze_mixed(self):
        output = self._run('print("aaabba".toSqueeze())')
        assert output[-1] == "aba"
