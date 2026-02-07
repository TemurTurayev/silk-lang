"""
Tests for string .toAlternatingCase() method.
"""

from silk.interpreter import Interpreter


class TestStringToAlternatingCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toAlternatingCase_basic(self):
        output = self._run('print("hello".toAlternatingCase())')
        assert output[-1] == "hElLo"

    def test_toAlternatingCase_world(self):
        output = self._run('print("world".toAlternatingCase())')
        assert output[-1] == "wOrLd"
