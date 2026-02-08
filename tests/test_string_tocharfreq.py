"""
Tests for string .toCharFreq() method - character frequency.
"""

from silk.interpreter import Interpreter


class TestStringToCharFreq:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toCharFreq_hello(self):
        output = self._run('print("hello".toCharFreq())')
        assert output[-1] == "h:1 e:1 l:2 o:1"

    def test_toCharFreq_aab(self):
        output = self._run('print("aab".toCharFreq())')
        assert output[-1] == "a:2 b:1"
