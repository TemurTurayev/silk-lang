"""
Tests for string .hamming() method.
"""

from silk.interpreter import Interpreter


class TestStringHamming:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_hamming_same(self):
        output = self._run('print("hello".hamming("hello"))')
        assert output[-1] == "0"

    def test_hamming_one_diff(self):
        output = self._run('print("hello".hamming("hallo"))')
        assert output[-1] == "1"

    def test_hamming_all_diff(self):
        output = self._run('print("abc".hamming("xyz"))')
        assert output[-1] == "3"
