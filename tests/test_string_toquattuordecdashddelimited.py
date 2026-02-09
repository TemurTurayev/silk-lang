"""
Tests for string .toQuattuordecDashDelimited() method - join words with 14 dashes.
"""

from silk.interpreter import Interpreter


class TestStringToQuattuordecDashDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuattuordecDashDelimited_basic(self):
        output = self._run('print("hello world".toQuattuordecDashDelimited())')
        assert output[-1] == "hello--------------world"

    def test_toQuattuordecDashDelimited_three(self):
        output = self._run('print("a b c".toQuattuordecDashDelimited())')
        assert output[-1] == "a--------------b--------------c"
