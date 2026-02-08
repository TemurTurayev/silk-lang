"""
Tests for array .mapDistinct() method - remove duplicates preserving order.
"""

from silk.interpreter import Interpreter


class TestArrayMapDistinct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDistinct_basic(self):
        output = self._run('''
let result = [1, 2, 2, 3, 3, 3].mapDistinct()
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_mapDistinct_already_unique(self):
        output = self._run('''
let result = [1, 2, 3].mapDistinct()
print(result)
''')
        assert output[-1] == "[1, 2, 3]"
