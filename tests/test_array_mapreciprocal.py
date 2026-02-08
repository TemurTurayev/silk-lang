"""
Tests for array .mapReciprocal() method - reciprocal of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapReciprocal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapReciprocal_basic(self):
        output = self._run('print([1, 2, 4].mapReciprocal())')
        assert output[-1] == "[1, 0.5, 0.25]"

    def test_mapReciprocal_single(self):
        output = self._run('print([5].mapReciprocal())')
        assert output[-1] == "[0.2]"
