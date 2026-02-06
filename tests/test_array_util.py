"""
Tests for array .enumerate(), .take(), .skip() methods.
"""

from silk.interpreter import Interpreter


class TestArrayEnumerate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_enumerate_basic(self):
        output = self._run('''
let arr = ["a", "b", "c"]
let pairs = arr.enumerate()
print(pairs.length)
''')
        assert output[-1] == "3"

    def test_enumerate_destructure(self):
        output = self._run('''
let arr = ["x", "y"]
for pair in arr.enumerate() {
    let [i, val] = pair
    print(f"{i}:{val}")
}
''')
        assert output == ["0:x", "1:y"]

    def test_enumerate_empty(self):
        output = self._run('''
print([].enumerate())
''')
        assert output[-1] == "[]"


class TestArrayTake:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_take_basic(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr.take(3))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_take_more_than_length(self):
        output = self._run('''
print([1, 2].take(10))
''')
        assert output[-1] == "[1, 2]"

    def test_take_zero(self):
        output = self._run('''
print([1, 2, 3].take(0))
''')
        assert output[-1] == "[]"


class TestArraySkip:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_skip_basic(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr.skip(2))
''')
        assert output[-1] == "[3, 4, 5]"

    def test_skip_all(self):
        output = self._run('''
print([1, 2, 3].skip(5))
''')
        assert output[-1] == "[]"

    def test_skip_zero(self):
        output = self._run('''
print([1, 2, 3].skip(0))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_take_and_skip_chained(self):
        output = self._run('''
let arr = 0..10
print(arr.skip(3).take(4))
''')
        assert output[-1] == "[3, 4, 5, 6]"
