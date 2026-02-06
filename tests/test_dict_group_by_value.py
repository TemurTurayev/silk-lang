"""
Tests for dict .groupByValue() method.
"""

from silk.interpreter import Interpreter


class TestDictGroupByValue:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_groupByValue_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 1}
let g = d.groupByValue()
print(g[1])
print(g[2])
''')
        assert output[0] == "[a, c]"
        assert output[1] == "[b]"

    def test_groupByValue_unique(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
let g = d.groupByValue()
print(g[1])
''')
        assert output[-1] == "[x]"
