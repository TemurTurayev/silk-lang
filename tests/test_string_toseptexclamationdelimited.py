"""
Tests for string .toSeptExclamationDelimited() method - split words by !!!!!!!.
"""

from silk.interpreter import Interpreter


class TestStringToSeptExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSeptExclamationDelimited_basic(self):
        output = self._run('print("hello world".toSeptExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!world"

    def test_toSeptExclamationDelimited_three(self):
        output = self._run('print("a b c".toSeptExclamationDelimited())')
        assert output[-1] == "a!!!!!!!b!!!!!!!c"
