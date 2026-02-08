"""
Tests for array .mapInits() method - all prefixes of the array.
"""

from silk.interpreter import Interpreter


class TestArrayMapInits:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapInits_basic(self):
        output = self._run('''
let result = [1, 2, 3].mapInits()
print(result)
''')
        assert output[-1] == "[[1], [1, 2], [1, 2, 3]]"

    def test_mapInits_two(self):
        output = self._run('''
let result = [4, 5].mapInits()
print(result)
''')
        assert output[-1] == "[[4], [4, 5]]"
