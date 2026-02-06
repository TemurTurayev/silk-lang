"""
Tests for array .partition() method - splits into [matches, non-matches].
"""

from silk.interpreter import Interpreter


class TestArrayPartition:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_partition_basic(self):
        output = self._run('''
let parts = [1, 2, 3, 4, 5].partition(|x| x > 3)
print(parts)
''')
        assert output[-1] == "[[4, 5], [1, 2, 3]]"

    def test_partition_even_odd(self):
        output = self._run('''
let parts = [1, 2, 3, 4].partition(|x| x % 2 == 0)
print(parts[0])
print(parts[1])
''')
        assert output[-2] == "[2, 4]"
        assert output[-1] == "[1, 3]"

    def test_partition_all_match(self):
        output = self._run('''
let parts = [2, 4, 6].partition(|x| x % 2 == 0)
print(parts[0])
print(parts[1])
''')
        assert output[-2] == "[2, 4, 6]"
        assert output[-1] == "[]"

    def test_partition_none_match(self):
        output = self._run('''
let parts = [1, 3, 5].partition(|x| x % 2 == 0)
print(parts[0])
print(parts[1])
''')
        assert output[-2] == "[]"
        assert output[-1] == "[1, 3, 5]"

    def test_partition_empty(self):
        output = self._run('''
print([].partition(|x| x > 0))
''')
        assert output[-1] == "[[], []]"
