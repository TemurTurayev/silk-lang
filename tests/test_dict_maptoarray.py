"""
Tests for dict .mapToArray(fn) method.
"""

from silk.interpreter import Interpreter


class TestDictMapToArray:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapToArray_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.mapToArray(|k, v| v * 10))
''')
        assert output[-1] == "[10, 20]"

    def test_mapToArray_strings(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
print(d.mapToArray(|k, v| k))
''')
        assert output[-1] == "[x, y]"
