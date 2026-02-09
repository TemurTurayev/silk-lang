"""
Tests for string .toQuattuordecAmpersandDelimited() method - join words with 14 ampersands.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecAmpersandDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecAmpersandDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecAmpersandDelimited())')
        assert output[-1] == "hello&&&&&&&&&&&&&&world"

    def test_toQuattuordecAmpersandDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecAmpersandDelimited())')
        assert output[-1] == "a&&&&&&&&&&&&&&b&&&&&&&&&&&&&&c"
