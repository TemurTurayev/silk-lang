"""
Tests for string .toAbbreviation() method - first letter of each word uppercased.
"""

from silk.interpreter import Interpreter


class TestStringToAbbreviation:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAbbreviation_basic(self):
        output = self._run('print("Hello World".toAbbreviation())')
        assert output[-1] == "HW"

    def test_toAbbreviation_three_words(self):
        output = self._run('print("first second third".toAbbreviation())')
        assert output[-1] == "FST"
