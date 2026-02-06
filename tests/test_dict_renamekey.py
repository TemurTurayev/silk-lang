"""
Tests for dict .renameKey(old, new) method.
"""

from silk.interpreter import Interpreter


class TestDictRenameKey:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_renameKey_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
let d2 = d.renameKey("name", "fullName")
print(d2["fullName"])
print(d2["age"])
''')
        assert output[0] == "Alice"
        assert output[1] == "30"

    def test_renameKey_missing(self):
        output = self._run('''
let d = {"x": 1}
let d2 = d.renameKey("y", "z")
print(d2["x"])
''')
        assert output[-1] == "1"
