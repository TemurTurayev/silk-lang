"""
Tests for dict .pick(), .omit(), and .invert() methods.
"""

from silk.interpreter import Interpreter


class TestDictPick:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_pick_basic(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let picked = m.pick(["a", "c"])
print(picked.get("a"))
print(picked.get("c"))
print(picked.length)
''')
        assert output[-3] == "1"
        assert output[-2] == "3"
        assert output[-1] == "2"

    def test_omit_basic(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
let omitted = m.omit(["b"])
print(omitted.length)
print(omitted.has("b"))
''')
        assert output[-2] == "2"
        assert output[-1] == "false"

    def test_invert(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let inv = m.invert()
print(inv.get(1))
print(inv.get(2))
''')
        assert output[-2] == "a"
        assert output[-1] == "b"
