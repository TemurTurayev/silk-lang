"""
Tests for zip() builtin function.
"""

from silk.interpreter import Interpreter


class TestZip:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zip_basic(self):
        output = self._run('''
let names = ["Alice", "Bob"]
let ages = [30, 25]
let zipped = zip(names, ages)
print(zipped)
''')
        assert output[-1] == "[[Alice, 30], [Bob, 25]]"

    def test_zip_different_lengths(self):
        """Zip stops at shorter array."""
        output = self._run('''
let a = [1, 2, 3]
let b = [10, 20]
print(zip(a, b))
''')
        assert output[-1] == "[[1, 10], [2, 20]]"

    def test_zip_empty(self):
        output = self._run('''
print(zip([], [1, 2]))
''')
        assert output[-1] == "[]"

    def test_zip_with_range(self):
        output = self._run('''
let indexed = zip(0..3, ["a", "b", "c"])
print(indexed)
''')
        assert output[-1] == "[[0, a], [1, b], [2, c]]"

    def test_zip_with_destructure(self):
        output = self._run('''
let pairs = zip(["x", "y"], [1, 2])
for pair in pairs {
    let [name, val] = pair
    print(f"{name}={val}")
}
''')
        assert output[0] == "x=1"
        assert output[1] == "y=2"
