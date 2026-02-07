"""
Tests for number .isPowerOfTwo() method.
"""

from silk.interpreter import Interpreter


class TestNumberIsPowerOfTwo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPowerOfTwo_true(self):
        output = self._run('print(8.isPowerOfTwo())')
        assert output[-1] == "true"

    def test_isPowerOfTwo_one(self):
        output = self._run('print(1.isPowerOfTwo())')
        assert output[-1] == "true"

    def test_isPowerOfTwo_false(self):
        output = self._run('print(6.isPowerOfTwo())')
        assert output[-1] == "false"
