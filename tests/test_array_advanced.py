"""
Tests for array .sortBy() and .groupBy() methods.
"""

from silk.interpreter import Interpreter


class TestArraySortBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sortBy_number(self):
        output = self._run('''
struct Item { name, price }
let a = Item { name: "C", price: 30 }
let b = Item { name: "A", price: 10 }
let c = Item { name: "B", price: 20 }
let items = [a, b, c]
let sorted = items.sortBy(|x| x.price)
for item in sorted {
    print(item.name)
}
''')
        assert output == ["A", "B", "C"]

    def test_sortBy_string_length(self):
        output = self._run('''
let words = ["hello", "hi", "hey"]
let sorted = words.sortBy(|w| w.length)
print(sorted)
''')
        assert output[-1] == "[hi, hey, hello]"

    def test_sortBy_identity(self):
        output = self._run('''
let nums = [3, 1, 2]
print(nums.sortBy(|x| x))
''')
        assert output[-1] == "[1, 2, 3]"


class TestArrayGroupBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_groupBy_basic(self):
        output = self._run('''
let items = [1, 2, 3, 4, 5, 6]
let groups = items.groupBy(|x| x % 2 == 0)
print(groups.keys().length)
''')
        assert output[-1] == "2"

    def test_groupBy_strings(self):
        output = self._run('''
let words = ["apple", "avocado", "banana", "blueberry"]
let groups = words.groupBy(|w| w.charAt(0))
print(groups.has("a"))
print(groups.has("b"))
''')
        assert output[-2] == "true"
        assert output[-1] == "true"

    def test_groupBy_empty(self):
        output = self._run('''
let groups = [].groupBy(|x| x)
print(groups.length)
''')
        assert output[-1] == "0"

    def test_groupBy_count(self):
        output = self._run('''
let nums = [1, 1, 2, 2, 2, 3]
let groups = nums.groupBy(|x| x)
print(groups.keys().length)
''')
        assert output[-1] == "3"
