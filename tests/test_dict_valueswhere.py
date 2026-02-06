"""
Tests for dict .valuesWhere(fn) method.
"""

from silk.interpreter import Interpreter


class TestDictValuesWhere:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_valuesWhere_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 5, "c": 3, "d": 8}
print(d.valuesWhere(|k, v| v > 3))
''')
        assert output[-1] == "[5, 8]"

    def test_valuesWhere_none(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.valuesWhere(|k, v| v > 10))
''')
        assert output[-1] == "[]"
