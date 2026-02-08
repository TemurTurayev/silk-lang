"""
Tests for array .mapHeads() method - all prefixes of the array.
"""

from silk.interpreter import Interpreter


class TestArrayMapHeads:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapHeads_basic(self):
        output = self._run('''
let result = [1, 2, 3].mapHeads()
print(result)
''')
        assert output[-1] == "[[1], [1, 2], [1, 2, 3]]"

    def test_mapHeads_two(self):
        output = self._run('''
let result = [4, 5].mapHeads()
print(result)
''')
        assert output[-1] == "[[4], [4, 5]]"
