"""
Tests for string .toInitials() method - first letter of each word with dots.
"""

from silk.interpreter import Interpreter


class TestStringToInitials:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInitials_basic(self):
        output = self._run('print("John Smith".toInitials())')
        assert output[-1] == "J.S."

    def test_toInitials_three_words(self):
        output = self._run('print("John Michael Smith".toInitials())')
        assert output[-1] == "J.M.S."
