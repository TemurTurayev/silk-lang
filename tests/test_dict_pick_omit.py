"""
Tests for dict .pick() and .omit() methods.
"""

from silk.interpreter import Interpreter


class TestDictPickOmit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pick_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
let result = d.pick(["a", "c"])
print(result.length)
print(result.get("a"))
print(result.get("c"))
''')
        assert output[-3] == "2"
        assert output[-2] == "1"
        assert output[-1] == "3"

    def test_omit_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
let result = d.omit(["b"])
print(result.length)
print(result.get("a"))
print(result.get("c"))
''')
        assert output[-3] == "2"
        assert output[-2] == "1"
        assert output[-1] == "3"

    def test_pick_empty(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
let result = d.pick([])
print(result.length)
''')
        assert output[-1] == "0"
