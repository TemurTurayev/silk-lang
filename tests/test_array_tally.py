"""
Tests for array .tally() - count occurrences of each value.
"""

from silk.interpreter import Interpreter


class TestArrayTally:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_tally_basic(self):
        output = self._run('''
let counts = ["a", "b", "a", "c", "b", "a"].tally()
print(counts.get("a"))
print(counts.get("b"))
print(counts.get("c"))
''')
        assert output[-3] == "3"
        assert output[-2] == "2"
        assert output[-1] == "1"

    def test_tally_numbers(self):
        output = self._run('''
let counts = [1, 2, 1, 1, 3, 2].tally()
print(counts.get(1))
print(counts.get(2))
print(counts.get(3))
''')
        assert output[-3] == "3"
        assert output[-2] == "2"
        assert output[-1] == "1"

    def test_tally_empty(self):
        output = self._run('''
let counts = [].tally()
print(counts.length)
''')
        assert output[-1] == "0"

    def test_tally_single(self):
        output = self._run('''
let counts = ["x"].tally()
print(counts.get("x"))
''')
        assert output[-1] == "1"
