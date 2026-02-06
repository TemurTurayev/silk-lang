"""
Tests for dict .countValues() method.
"""

from silk.interpreter import Interpreter


class TestDictCountValues:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countValues_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1}
print(d.countValues())
''')
        assert output[-1] == '{1: 3, 2: 2}'

    def test_countValues_unique(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.countValues())
''')
        assert output[-1] == '{1: 1, 2: 1, 3: 1}'
