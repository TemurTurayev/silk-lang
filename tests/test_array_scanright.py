"""
Tests for array .scanRight(fn, init) method - scan from right.
"""

from silk.interpreter import Interpreter


class TestArrayScanRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_scanRight_sum(self):
        output = self._run('''
let result = [1, 2, 3].scanRight(|acc, x| acc + x, 0)
print(result)
''')
        assert output[-1] == "[6, 5, 3]"

    def test_scanRight_multiply(self):
        output = self._run('''
let result = [1, 2, 3].scanRight(|acc, x| acc * x, 1)
print(result)
''')
        assert output[-1] == "[6, 6, 3]"
