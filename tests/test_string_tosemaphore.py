"""
Tests for string .toSemaphore() method - convert to flag semaphore positions.
"""

from silk.interpreter import Interpreter


class TestStringToSemaphore:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSemaphore_ab(self):
        output = self._run('print("ab".toSemaphore())')
        assert output[-1] == "1 2"

    def test_toSemaphore_hi(self):
        output = self._run('print("hi".toSemaphore())')
        assert output[-1] == "8 9"
