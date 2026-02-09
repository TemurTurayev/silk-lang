"""
Tests for string .toDuodecExclamationDelimited() method - split words by !!!!!!!!!!!! (12 exclamations).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecExclamationDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecExclamationDelimited_basic(self):
        output = self._run('print("hello world".toDuodecExclamationDelimited())')
        assert output[-1] == "hello!!!!!!!!!!!!world"

    def test_toDuodecExclamationDelimited_three(self):
        output = self._run('print("a b c".toDuodecExclamationDelimited())')
        assert output[-1] == "a!!!!!!!!!!!!b!!!!!!!!!!!!c"
