"""
Tests for array .countRight(fn) method - count matching from right.
"""

from silk.interpreter import Interpreter


class TestArrayCountRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countRight_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].countRight(|x| x > 3)
print(result)
''')
        assert output[-1] == "2"

    def test_countRight_all(self):
        output = self._run('''
let result = [1, 2, 3].countRight(|x| x > 0)
print(result)
''')
        assert output[-1] == "3"
