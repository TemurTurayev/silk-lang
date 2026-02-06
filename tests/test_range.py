"""
Tests for range expression (1..5).

Syntax: start..end (inclusive of start, exclusive of end)
"""

from silk.interpreter import Interpreter


class TestRangeExpression:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_range(self):
        output = self._run('''
let r = 1..5
print(r)
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_range_zero_start(self):
        output = self._run('''
let r = 0..3
print(r)
''')
        assert output[-1] == "[0, 1, 2]"

    def test_range_in_for_loop(self):
        output = self._run('''
let mut sum = 0
for i in 1..6 {
    sum += i
}
print(sum)
''')
        assert output[-1] == "15"

    def test_range_single_element(self):
        output = self._run('''
let r = 5..6
print(r)
''')
        assert output[-1] == "[5]"

    def test_range_empty(self):
        output = self._run('''
let r = 5..5
print(r)
''')
        assert output[-1] == "[]"

    def test_range_with_variables(self):
        output = self._run('''
let start = 2
let end = 7
let r = start..end
print(r.length)
''')
        assert output[-1] == "5"

    def test_range_with_spread(self):
        output = self._run('''
let r = [0, ...1..4, 99]
print(r)
''')
        assert output[-1] == "[0, 1, 2, 3, 99]"

    def test_range_map(self):
        output = self._run('''
let squares = (0..5).map(fn(x) { return x * x })
print(squares)
''')
        assert output[-1] == "[0, 1, 4, 9, 16]"
