"""
Tests for dict .invert() method.
"""

from silk.interpreter import Interpreter


class TestDictInvert:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_invert_basic(self):
        output = self._run('''
let d = {"a": 1, "b": 2, "c": 3}
let inv = d.invert()
print(inv.get(1))
print(inv.get(2))
print(inv.get(3))
''')
        assert output[-3] == "a"
        assert output[-2] == "b"
        assert output[-1] == "c"

    def test_invert_strings(self):
        output = self._run('''
let d = {"name": "alice", "role": "admin"}
let inv = d.invert()
print(inv.get("alice"))
print(inv.get("admin"))
''')
        assert output[-2] == "name"
        assert output[-1] == "role"

    def test_invert_length(self):
        output = self._run('''
let d = {"x": 10, "y": 20}
let inv = d.invert()
print(inv.length)
''')
        assert output[-1] == "2"
