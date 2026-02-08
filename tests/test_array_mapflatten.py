"""
Tests for array .mapFlatten() method - flatten one level deep.
"""

from silk.interpreter import Interpreter


class TestArrayMapFlatten:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFlatten_basic(self):
        output = self._run('''
let result = [[1, 2], [3, 4]].mapFlatten()
print(result)
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_mapFlatten_mixed(self):
        output = self._run('''
let result = [[1], 2, [3, 4]].mapFlatten()
print(result)
''')
        assert output[-1] == "[1, 2, 3, 4]"
