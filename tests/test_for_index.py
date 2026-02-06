"""
Tests for indexed for loop.

Syntax: for i, val in iterable { ... }
"""

from silk.interpreter import Interpreter


class TestForIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_indexed_for(self):
        output = self._run('''
let arr = ["a", "b", "c"]
for i, val in arr {
    print(f"{i}: {val}")
}
''')
        assert output == ["0: a", "1: b", "2: c"]

    def test_indexed_for_sum(self):
        output = self._run('''
let arr = [10, 20, 30]
let mut total = 0
for i, val in arr {
    total += val * i
}
print(total)
''')
        assert output[-1] == "80"

    def test_indexed_for_with_range(self):
        output = self._run('''
let items = ["x", "y", "z"]
for i, item in items {
    if i == 1 {
        print(item)
    }
}
''')
        assert output[-1] == "y"

    def test_indexed_for_empty(self):
        output = self._run('''
let arr = []
for i, val in arr {
    print("should not run")
}
print("done")
''')
        assert output == ["done"]

    def test_regular_for_still_works(self):
        """Non-indexed for loop should still work."""
        output = self._run('''
for x in [1, 2, 3] {
    print(x)
}
''')
        assert output == ["1", "2", "3"]

    def test_indexed_for_break(self):
        output = self._run('''
for i, val in [10, 20, 30, 40] {
    if i >= 2 { break }
    print(val)
}
''')
        assert output == ["10", "20"]
