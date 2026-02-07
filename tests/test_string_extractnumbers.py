"""
Tests for string .extractNumbers() method.
"""

from silk.interpreter import Interpreter


class TestStringExtractNumbers:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_extractNumbers_basic(self):
        output = self._run('print("abc123def456".extractNumbers())')
        assert output[-1] == "[123, 456]"

    def test_extractNumbers_none(self):
        output = self._run('print("hello".extractNumbers())')
        assert output[-1] == "[]"

    def test_extractNumbers_mixed(self):
        output = self._run('print("I have 3 cats and 2 dogs".extractNumbers())')
        assert output[-1] == "[3, 2]"
