"""
Tests for array .groupBy() method.
"""

from silk.interpreter import Interpreter


class TestArrayGroupBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_groupBy_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5, 6].groupBy(|n| if n % 2 == 0 then "even" else "odd")
print(result.get("even"))
print(result.get("odd"))
''')
        assert output[-2] == "[2, 4, 6]"
        assert output[-1] == "[1, 3, 5]"

    def test_groupBy_strings(self):
        output = self._run('''
let result = ["apple", "avocado", "banana", "blueberry"].groupBy(|s| s.charAt(0))
print(result.get("a").length)
print(result.get("b").length)
''')
        assert output[-2] == "2"
        assert output[-1] == "2"

    def test_groupBy_length(self):
        output = self._run('''
let result = ["a", "bb", "c", "dd"].groupBy(|s| s.length)
print(result.length)
''')
        assert output[-1] == "2"
