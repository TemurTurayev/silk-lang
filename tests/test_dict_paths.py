"""
Tests for dict .paths() method.
"""

from silk.interpreter import Interpreter


class TestDictPaths:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_paths_flat(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
print(d.paths())
''')
        assert output[-1] == "[a, b]"

    def test_paths_nested(self):
        output = self._run('''
let d = {"a": 1, "b": {"c": 2, "d": 3}}
print(d.paths())
''')
        assert output[-1] == "[a, b.c, b.d]"
