"""
Tests for array .symmetricDifference() method.
"""

from silk.interpreter import Interpreter


class TestArraySymDiff:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_symdiff_basic(self):
        output = self._run('''
print([1, 2, 3].symmetricDifference([2, 3, 4]))
''')
        assert output[-1] == "[1, 4]"

    def test_symdiff_no_overlap(self):
        output = self._run('''
print([1, 2].symmetricDifference([3, 4]))
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_symdiff_same(self):
        output = self._run('''
print([1, 2, 3].symmetricDifference([1, 2, 3]))
''')
        assert output[-1] == "[]"
