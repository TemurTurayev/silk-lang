"""
Tests for string .toBackticked() method - wrap string in backticks.
"""

from silk.interpreter import Interpreter


class TestStringToBackticked:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBackticked_basic(self):
        output = self._run('print("code".toBackticked())')
        assert output[-1] == "`code`"

    def test_toBackticked_word(self):
        output = self._run('print("hello".toBackticked())')
        assert output[-1] == "`hello`"
