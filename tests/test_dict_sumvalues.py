"""
Tests for dict .sumValues() method.
"""

from silk.interpreter import Interpreter


class TestDictSumValues:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sumValues_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.sumValues())
''')
        assert output[-1] == '6'

    def test_sumValues_single(self):
        output = self._run('''
let d = {"x": 42}
print(d.sumValues())
''')
        assert output[-1] == '42'
