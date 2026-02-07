"""
Tests for dict .toTuples() method.
"""

from silk.interpreter import Interpreter


class TestDictToTuples:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toTuples_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.toTuples())
''')
        assert output[-1] == '[[a, 1], [b, 2]]'

    def test_toTuples_single(self):
        output = self._run('''
let d = {"x": 99}
print(d.toTuples())
''')
        assert output[-1] == '[[x, 99]]'
