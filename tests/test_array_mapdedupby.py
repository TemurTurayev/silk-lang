"""
Tests for array .mapDedupBy(fn) method - deduplicate by key function.
"""

from silk.interpreter import Interpreter


class TestArrayMapDedupBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDedupBy_identity(self):
        output = self._run('''
let result = [1, 2, 2, 3, 1].mapDedupBy(|x| x)
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_mapDedupBy_modulo(self):
        output = self._run('''
let result = [1, 3, 5, 2, 4].mapDedupBy(|x| x % 2)
print(result)
''')
        assert output[-1] == "[1, 2]"
