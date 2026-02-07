"""
Tests for array .forEachRight(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayForEachRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_forEachRight_basic(self):
        output = self._run('''
let result = []
[1, 2, 3].forEachRight(|x| result.push(x))
print(result)
''')
        assert output[-1] == "[3, 2, 1]"
