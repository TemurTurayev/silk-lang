"""
Tests for string .toBacon() method - Bacon's cipher (a=AAAAA, b=AAAAB, etc).
"""

from silk.interpreter import Interpreter


class TestStringToBacon:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBacon_ab(self):
        output = self._run('print("ab".toBacon())')
        assert output[-1] == "AAAAA AAAAB"

    def test_toBacon_hi(self):
        output = self._run('print("hi".toBacon())')
        assert output[-1] == "AABBB ABAAA"
