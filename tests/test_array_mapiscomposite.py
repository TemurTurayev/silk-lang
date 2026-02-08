"""
Tests for array .mapIsComposite() method - check if each element is composite.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsComposite:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsComposite_mixed(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].mapIsComposite())')
        assert output[-1] == "[false, false, false, true, false, true]"

    def test_mapIsComposite_allComposite(self):
        output = self._run('print([4, 6, 8, 9].mapIsComposite())')
        assert output[-1] == "[true, true, true, true]"
