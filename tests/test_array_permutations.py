"""
Tests for array .permutations() method.
"""

from silk.interpreter import Interpreter


class TestArrayPermutations:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_permutations_basic(self):
        output = self._run('''
let p = [1, 2, 3].permutations()
print(p.length)
''')
        assert output[-1] == "6"

    def test_permutations_pair(self):
        output = self._run('''
let p = [1, 2].permutations()
print(p[0])
print(p[1])
''')
        assert output[0] == "[1, 2]"
        assert output[1] == "[2, 1]"

    def test_permutations_single(self):
        output = self._run('''
print([1].permutations())
''')
        assert output[-1] == "[[1]]"
