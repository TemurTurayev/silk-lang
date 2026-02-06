"""
Tests for array .pairwise() and .interleave() methods.
"""

from silk.interpreter import Interpreter


class TestArrayPairwise:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pairwise_basic(self):
        output = self._run('''
print([1, 2, 3, 4].pairwise())
''')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_pairwise_short(self):
        output = self._run('''
print([1].pairwise())
''')
        assert output[-1] == "[]"

    def test_pairwise_two(self):
        output = self._run('''
print([1, 2].pairwise())
''')
        assert output[-1] == "[[1, 2]]"


class TestArrayInterleave:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_interleave_basic(self):
        output = self._run('''
print([1, 2, 3].interleave(["a", "b", "c"]))
''')
        assert output[-1] == "[1, a, 2, b, 3, c]"

    def test_interleave_unequal(self):
        output = self._run('''
print([1, 2].interleave(["a", "b", "c"]))
''')
        assert output[-1] == "[1, a, 2, b, c]"

    def test_interleave_empty(self):
        output = self._run('''
print([].interleave([1, 2]))
''')
        assert output[-1] == "[1, 2]"
