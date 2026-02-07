"""
Tests for string .wordFrequency() method.
"""

from silk.interpreter import Interpreter


class TestStringWordFrequency:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_wordFrequency_basic(self):
        output = self._run('print("the cat sat on the mat".wordFrequency())')
        assert output[-1] == '{"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}'

    def test_wordFrequency_single(self):
        output = self._run('print("hello".wordFrequency())')
        assert output[-1] == '{"hello": 1}'

    def test_wordFrequency_empty(self):
        output = self._run('print("".wordFrequency())')
        assert output[-1] == '{}'
