"""
Tests for negative indexing on arrays and strings.
"""

from silk.interpreter import Interpreter


class TestNegativeIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_array_last(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr[-1])
''')
        assert output[-1] == "5"

    def test_array_second_last(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5]
print(arr[-2])
''')
        assert output[-1] == "4"

    def test_array_negative_first(self):
        output = self._run('''
let arr = [10, 20, 30]
print(arr[-3])
''')
        assert output[-1] == "10"

    def test_string_last_char(self):
        output = self._run('''
print("hello"[-1])
''')
        assert output[-1] == "o"

    def test_string_second_last(self):
        output = self._run('''
print("hello"[-2])
''')
        assert output[-1] == "l"

    def test_negative_index_assign(self):
        output = self._run('''
let mut arr = [1, 2, 3]
arr[-1] = 99
print(arr)
''')
        assert output[-1] == "[1, 2, 99]"
