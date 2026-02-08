"""
Tests for array .mapToOctal() method - convert each element to octal.
"""

from silk.interpreter import Interpreter


class TestArrayMapToOctal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToOctal_basic(self):
        output = self._run('print([1, 8, 9, 64].mapToOctal())')
        # 1->1, 8->10, 9->11, 64->100
        assert output[-1] == "[1, 10, 11, 100]"

    def test_mapToOctal_small(self):
        output = self._run('print([7, 15, 16].mapToOctal())')
        # 7->7, 15->17, 16->20
        assert output[-1] == "[7, 17, 20]"
