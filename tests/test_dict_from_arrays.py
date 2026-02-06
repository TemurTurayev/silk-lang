"""
Tests for Dict.fromArrays() static method.
"""

from silk.interpreter import Interpreter


class TestDictFromArrays:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fromArrays_basic(self):
        output = self._run('''
let d = Dict.fromArrays(["a", "b", "c"], [1, 2, 3])
print(d.get("a"))
print(d.get("b"))
print(d.get("c"))
''')
        assert output[-3] == "1"
        assert output[-2] == "2"
        assert output[-1] == "3"

    def test_fromArrays_length(self):
        output = self._run('''
let d = Dict.fromArrays(["x", "y"], [10, 20])
print(d.length)
''')
        assert output[-1] == "2"

    def test_fromArrays_empty(self):
        output = self._run('''
let d = Dict.fromArrays([], [])
print(d.length)
''')
        assert output[-1] == "0"
