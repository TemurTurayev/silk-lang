"""
Tests for dict .deepMerge(other) method.
"""

from silk.interpreter import Interpreter


class TestDictDeepMerge:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_deepMerge_flat(self):
        output = self._run('''
let a = {"x": 1, "y": 2}
let b = {"y": 3, "z": 4}
let c = a.deepMerge(b)
print(c["x"])
print(c["y"])
print(c["z"])
''')
        assert output[0] == "1"
        assert output[1] == "3"
        assert output[2] == "4"

    def test_deepMerge_nested(self):
        output = self._run('''
let a = {"a": {"x": 1, "y": 2}}
let b = {"a": {"y": 3, "z": 4}}
let c = a.deepMerge(b)
print(c["a"]["x"])
print(c["a"]["y"])
print(c["a"]["z"])
''')
        assert output[0] == "1"
        assert output[1] == "3"
        assert output[2] == "4"
