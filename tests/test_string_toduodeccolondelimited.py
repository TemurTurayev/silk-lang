"""
Tests for string .toDuodecColonDelimited() method - split words by :::::::::::: (12 colons).
"""

from silk.interpreter import Interpreter


class TestStringToDuodecColonDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toDuodecColonDelimited_basic(self):
        output = self._run('print("hello world".toDuodecColonDelimited())')
        assert output[-1] == "hello::::::::::::world"

    def test_toDuodecColonDelimited_three(self):
        output = self._run('print("a b c".toDuodecColonDelimited())')
        assert output[-1] == "a::::::::::::b::::::::::::c"
