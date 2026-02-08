"""
Tests for array .mapUniq() method - remove duplicates preserving order.
"""

from silk.interpreter import Interpreter


class TestArrayMapUniq:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapUniq_basic(self):
        output = self._run('''
let result = [1, 2, 2, 3, 1].mapUniq()
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_mapUniq_no_dupes(self):
        output = self._run('''
let result = [4, 5, 6].mapUniq()
print(result)
''')
        assert output[-1] == "[4, 5, 6]"
