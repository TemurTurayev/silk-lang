"""
Tests for string .toQuadExclamationDelimited() method - split words by !!!!.
"""

from silk.interpreter import Interpreter


class TestStringToQuadExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQuadExclamationDelimited_basic(self):
        output = self._run('print("hello world".toQuadExclamationDelimited())')
        assert output[-1] == "hello!!!!world"

    def test_toQuadExclamationDelimited_three(self):
        output = self._run('print("a b c".toQuadExclamationDelimited())')
        assert output[-1] == "a!!!!b!!!!c"
