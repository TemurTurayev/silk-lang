"""
Tests for string .toSpongeCase() method - alternating case.
"""

from silk.interpreter import Interpreter


class TestStringToSpongeCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSpongeCase_hello(self):
        output = self._run('print("hello".toSpongeCase())')
        assert output[-1] == "hElLo"

    def test_toSpongeCase_abc(self):
        output = self._run('print("abcde".toSpongeCase())')
        assert output[-1] == "aBcDe"
