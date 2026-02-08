"""
Tests for string .toDecExclamationDelimited() method - split words by !!!!!!!!!! (10 exclamations).
"""

from silk.interpreter import Interpreter


class TestStringToDecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toDecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!world"

    def test_toDecExclamationDelimited_three(self):
        output = self._run('print("a b c".toDecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!b!!!!!!!!!!c"
