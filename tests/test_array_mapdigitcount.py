"""
Tests for array .mapDigitCount() method - count digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitCount_basic(self):
        output = self._run('print([1, 12, 123, 1234].mapDigitCount())')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_mapDigitCount_large(self):
        output = self._run('print([100, 9999, 5].mapDigitCount())')
        assert output[-1] == "[3, 4, 1]"
