"""
Tests for string .toSextUnderscoreDelimited() method - split words by ______.
"""

from silk.interpreter import Interpreter


class TestStringToSextUnderscoreDelimited:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSextUnderscoreDelimited_basic(self):
        output = self._run('print("hello world".toSextUnderscoreDelimited())')
        assert output[-1] == "hello______world"

    def test_toSextUnderscoreDelimited_three(self):
        output = self._run('print("a b c".toSextUnderscoreDelimited())')
        assert output[-1] == "a______b______c"
