"""
Tests for array .findRight(fn) method - find last matching element.
"""

from silk.interpreter import Interpreter


class TestArrayFindRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_findRight_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].findRight(|x| x < 4)
print(result)
''')
        assert output[-1] == "3"

    def test_findRight_string(self):
        output = self._run('''
let result = ["apple", "banana", "cherry"].findRight(|x| x.length() > 5)
print(result)
''')
        assert output[-1] == "cherry"
