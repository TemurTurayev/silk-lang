"""
Tests for array .mapConsecutive(n, fn) method - apply fn to consecutive groups of n.
"""

from silk.interpreter import Interpreter


class TestArrayMapConsecutive:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapConsecutive_sum_pairs(self):
        output = self._run('''
let result = [1, 2, 3, 4].mapConsecutive(2, |pair| pair[0] + pair[1])
print(result)
''')
        assert output[-1] == "[3, 5, 7]"

    def test_mapConsecutive_triples(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].mapConsecutive(3, |t| t[0] + t[1] + t[2])
print(result)
''')
        assert output[-1] == "[6, 9, 12]"
