"""
Tests for string .toLowerFirst() method - lowercase first char of each word.
"""

from silk.interpreter import Interpreter


class TestStringToLowerFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLowerFirst_basic(self):
        output = self._run('print("Hello World".toLowerFirst())')
        assert output[-1] == "hello world"

    def test_toLowerFirst_mixed(self):
        output = self._run('print("HELLO WORLD".toLowerFirst())')
        assert output[-1] == "hELLO wORLD"
