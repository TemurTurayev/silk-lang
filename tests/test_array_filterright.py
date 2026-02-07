"""
Tests for array .filterRight(fn) method - filter in reverse order.
"""

from silk.interpreter import Interpreter


class TestArrayFilterRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filterRight_basic(self):
        output = self._run('''
let result = [1, 2, 3, 4, 5].filterRight(|x| x > 2)
print(result)
''')
        assert output[-1] == "[5, 4, 3]"

    def test_filterRight_strings(self):
        output = self._run('''
let result = ["a", "bb", "ccc"].filterRight(|x| x.length() > 1)
print(result)
''')
        assert output[-1] == "[ccc, bb]"
