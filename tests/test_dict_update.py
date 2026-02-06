"""
Tests for dict .update() and .size() methods.
"""

from silk.interpreter import Interpreter


class TestDictUpdate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_update_basic(self):
        output = self._run('''
let a = {"x": 1, "y": 2}
let b = a.update({"y": 99, "z": 3})
print(b.get("x"))
print(b.get("y"))
print(b.get("z"))
''')
        assert output[-3] == "1"
        assert output[-2] == "99"
        assert output[-1] == "3"

    def test_update_no_mutation(self):
        output = self._run('''
let a = {"x": 1}
let b = a.update({"y": 2})
print(a.length)
print(b.length)
''')
        assert output[-2] == "1"
        assert output[-1] == "2"

    def test_size_alias(self):
        output = self._run('''
let m = {"a": 1, "b": 2, "c": 3}
print(m.size())
''')
        assert output[-1] == "3"
