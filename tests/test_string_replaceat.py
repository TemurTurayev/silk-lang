"""
Tests for string .replaceAt(index, char) method.
"""

from silk.interpreter import Interpreter


class TestStringReplaceAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_replaceAt_basic(self):
        output = self._run('print("hello".replaceAt(1, "a"))')
        assert output[-1] == "hallo"

    def test_replaceAt_first(self):
        output = self._run('print("abc".replaceAt(0, "X"))')
        assert output[-1] == "Xbc"
