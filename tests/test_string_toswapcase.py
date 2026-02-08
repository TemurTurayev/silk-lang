"""
Tests for string .toSwapCase() method - swap upper/lower case.
"""

from silk.interpreter import Interpreter


class TestStringToSwapCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSwapCase_basic(self):
        output = self._run('print("Hello World".toSwapCase())')
        assert output[-1] == "hELLO wORLD"

    def test_toSwapCase_all_upper(self):
        output = self._run('print("ABC".toSwapCase())')
        assert output[-1] == "abc"
