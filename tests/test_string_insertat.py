"""
Tests for string .insertAt(index, str) method.
"""

from silk.interpreter import Interpreter


class TestStringInsertAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_insertAt_basic(self):
        output = self._run('print("helo".insertAt(3, "l"))')
        assert output[-1] == "hello"

    def test_insertAt_start(self):
        output = self._run('print("world".insertAt(0, "hello "))')
        assert output[-1] == "hello world"
