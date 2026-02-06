"""
Tests for array .combinations(size) method.
"""

from silk.interpreter import Interpreter


class TestArrayCombinations:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_combinations_pairs(self):
        output = self._run('''
let c = [1, 2, 3].combinations(2)
print(c.length)
print(c[0])
print(c[1])
print(c[2])
''')
        assert output[0] == "3"
        assert output[1] == "[1, 2]"
        assert output[2] == "[1, 3]"
        assert output[3] == "[2, 3]"

    def test_combinations_singles(self):
        output = self._run('''
print([1, 2, 3].combinations(1).length)
''')
        assert output[-1] == "3"

    def test_combinations_full(self):
        output = self._run('''
print([1, 2, 3].combinations(3))
''')
        assert output[-1] == "[[1, 2, 3]]"
