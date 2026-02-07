"""
Tests for dict .pluck(keys) method.
"""

from silk.interpreter import Interpreter


class TestDictPluck:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pluck_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
print(d.pluck(["a", "c"]))
''')
        assert output[-1] == "[1, 3]"

    def test_pluck_single(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
print(d.pluck(["y"]))
''')
        assert output[-1] == "[20]"
