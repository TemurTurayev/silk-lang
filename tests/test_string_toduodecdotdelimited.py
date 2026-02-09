"""
Tests for string .toDuodecDotDelimited() method - split words by ............ (12 dots).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecDotDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecDotDelimited_basic(self):
        output = self._run('print("hello world".toDuodecDotDelimited())')
        assert output[-1] == "hello............world"

    def test_toDuodecDotDelimited_three(self):
        output = self._run('print("a b c".toDuodecDotDelimited())')
        assert output[-1] == "a............b............c"
