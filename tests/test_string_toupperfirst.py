"""
Tests for string .toUpperFirst() method - uppercase first char of each word.
"""

from silk.interpreter import Interpreter


class TestStringToUpperFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUpperFirst_basic(self):
        output = self._run('print("hello world".toUpperFirst())')
        assert output[-1] == "Hello World"

    def test_toUpperFirst_mixed(self):
        output = self._run('print("heLLO wORLD".toUpperFirst())')
        assert output[-1] == "HeLLO WORLD"
