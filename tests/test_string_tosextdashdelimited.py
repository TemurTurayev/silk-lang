"""
Tests for string .toSextDashDelimited() method - split words by ------.
"""

from silk.interpreter import Interpreter


class TestStringToSextDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextDashDelimited_basic(self):
        output = self._run('print("hello world".toSextDashDelimited())')
        assert output[-1] == "hello------world"

    def test_toSextDashDelimited_three(self):
        output = self._run('print("a b c".toSextDashDelimited())')
        assert output[-1] == "a------b------c"
