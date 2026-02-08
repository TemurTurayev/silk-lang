"""
Tests for array .mapStringify() method - convert each element to string.
"""

from silk.interpreter import Interpreter


class TestArrayMapStringify:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapStringify_basic(self):
        output = self._run('print([1, 2, 3].mapStringify())')
        assert output[-1] == '[1, 2, 3]'

    def test_mapStringify_mixed(self):
        output = self._run('print([true, 42].mapStringify())')
        assert output[-1] == '[true, 42]'
