"""
Tests for array .filterMapIndexed(fn) method - filter with index access.
"""

from silk.interpreter import Interpreter


class TestArrayFilterMapIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filterMapIndexed_even_index(self):
        output = self._run('''
let result = [10, 20, 30, 40].filterMapIndexed(|i, x| i % 2 == 0)
print(result)
''')
        assert output[-1] == "[10, 30]"

    def test_filterMapIndexed_gt(self):
        output = self._run('''
let result = [5, 10, 15, 20].filterMapIndexed(|i, x| x > i * 5)
print(result)
''')
        assert output[-1] == "[5, 10, 15, 20]"
