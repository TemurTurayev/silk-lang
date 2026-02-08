"""
Tests for string .toPigLatin() method - convert to Pig Latin.
"""

from silk.interpreter import Interpreter


class TestStringToPigLatin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPigLatin_hello(self):
        output = self._run('print("hello".toPigLatin())')
        assert output[-1] == "ellohay"

    def test_toPigLatin_apple(self):
        output = self._run('print("apple".toPigLatin())')
        assert output[-1] == "appleyay"
