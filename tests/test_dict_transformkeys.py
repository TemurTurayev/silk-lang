"""
Tests for dict .transformEntries(keyFn, valFn) method.
"""

from silk.interpreter import Interpreter


class TestDictTransformEntries:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_transformEntries_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.transformEntries(|k| k.toUpper(), |v| v * 10))
''')
        assert output[-1] == '{"A": 10, "B": 20}'

    def test_transformEntries_identity(self):
        output = self._run('''
let d = {"x": 5}
print(d.transformEntries(|k| k, |v| v))
''')
        assert output[-1] == '{"x": 5}'
