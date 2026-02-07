"""
Tests for array .mapRight(fn) method - map in reverse order.
"""

from silk.interpreter import Interpreter


class TestArrayMapRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRight_basic(self):
        output = self._run('''
let result = [1, 2, 3].mapRight(|x| x * 10)
print(result)
''')
        assert output[-1] == "[30, 20, 10]"

    def test_mapRight_strings(self):
        output = self._run('''
let result = ["a", "b", "c"].mapRight(|x| x.upper())
print(result)
''')
        assert output[-1] == "[C, B, A]"
