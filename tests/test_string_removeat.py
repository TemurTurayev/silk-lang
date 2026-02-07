"""
Tests for string .removeAt(index) method.
"""

from silk.interpreter import Interpreter


class TestStringRemoveAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removeAt_basic(self):
        output = self._run('print("hello".removeAt(1))')
        assert output[-1] == "hllo"

    def test_removeAt_first(self):
        output = self._run('print("abc".removeAt(0))')
        assert output[-1] == "bc"
