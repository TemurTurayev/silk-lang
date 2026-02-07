"""
Tests for dict .mapValuesWithKey(fn) method.
"""

from silk.interpreter import Interpreter


class TestDictMapValuesWithKey:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapValuesWithKey_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let r = d.mapValuesWithKey(|k, v| k + "=" + str(v))
print(r)
''')
        assert output[-1] == '{"a": a=1, "b": b=2}'

    def test_mapValuesWithKey_numbers(self):
        output = self._run('''
let d = {"x": 10}
let r = d.mapValuesWithKey(|k, v| v * 2)
print(r)
''')
        assert output[-1] == '{"x": 20}'
