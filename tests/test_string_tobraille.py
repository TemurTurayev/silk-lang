"""
Tests for string .toBraille() method - convert to Braille unicode characters.
"""

from silk.interpreter import Interpreter


class TestStringToBraille:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBraille_hi(self):
        output = self._run('print("hi".toBraille())')
        assert output[-1] == "\u2813\u280a"

    def test_toBraille_ab(self):
        output = self._run('print("ab".toBraille())')
        assert output[-1] == "\u2801\u2803"
