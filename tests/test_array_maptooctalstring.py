"""
Tests for array .mapToOctalString() method - convert each element to octal with 0o prefix.
"""

from silk.interpreter import Interpreter


class TestArrayMapToOctalString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToOctalString_basic(self):
        output = self._run('print([8, 64].mapToOctalString())')
        assert output[-1] == '[0o10, 0o100]'

    def test_mapToOctalString_small(self):
        output = self._run('print([0, 1, 7].mapToOctalString())')
        assert output[-1] == '[0o0, 0o1, 0o7]'
