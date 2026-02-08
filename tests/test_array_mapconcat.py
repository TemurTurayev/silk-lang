"""
Tests for array .mapConcat(fn) method - map and concatenate results.
"""

from silk.interpreter import Interpreter


class TestArrayMapConcat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapConcat_duplicate(self):
        output = self._run('''
let result = [1, 2, 3].mapConcat(|x| [x, x * 10])
print(result)
''')
        assert output[-1] == "[1, 10, 2, 20, 3, 30]"

    def test_mapConcat_single(self):
        output = self._run('''
let result = [5].mapConcat(|x| [x])
print(result)
''')
        assert output[-1] == "[5]"
