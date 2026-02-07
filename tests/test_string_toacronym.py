"""
Tests for string .toAcronym() method.
"""

from silk.interpreter import Interpreter


class TestStringToAcronym:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAcronym_basic(self):
        output = self._run('print("Hyper Text Markup Language".toAcronym())')
        assert output[-1] == "HTML"

    def test_toAcronym_lower(self):
        output = self._run('print("as soon as possible".toAcronym())')
        assert output[-1] == "ASAP"

    def test_toAcronym_single(self):
        output = self._run('print("Hello".toAcronym())')
        assert output[-1] == "H"
