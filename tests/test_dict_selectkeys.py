"""
Tests for dict .selectKeys(keys) method.
"""

from silk.interpreter import Interpreter


class TestDictSelectKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_selectKeys_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
let s = d.selectKeys(["a", "c"])
print(s["a"])
print(s["c"])
print(s.length)
''')
        assert output[0] == "1"
        assert output[1] == "3"
        assert output[2] == "2"

    def test_selectKeys_missing(self):
        output = self._run('''
let d = {"x": 10}
let s = d.selectKeys(["x", "y"])
print(s.length)
print(s["x"])
''')
        assert output[0] == "1"
        assert output[1] == "10"
