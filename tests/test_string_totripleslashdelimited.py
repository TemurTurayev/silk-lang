"""
Tests for string .toTripleSlashDelimited() method - split words by ///.
"""

from silk.interpreter import Interpreter


class TestStringToTripleSlashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTripleSlashDelimited_basic(self):
        output = self._run('print("hello world".toTripleSlashDelimited())')
        assert output[-1] == "hello///world"

    def test_toTripleSlashDelimited_three(self):
        output = self._run('print("a b c".toTripleSlashDelimited())')
        assert output[-1] == "a///b///c"
