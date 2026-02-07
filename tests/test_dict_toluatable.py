"""
Tests for dict .toLuaTable() method.
"""

from silk.interpreter import Interpreter


class TestDictToLuaTable:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLuaTable_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let lua = d.toLuaTable()
print(lua.contains("name"))
''')
        assert output[-1] == "true"

    def test_toLuaTable_braces(self):
        output = self._run('''
let d = {"x": 1}
let lua = d.toLuaTable()
print(lua.starts_with("{"))
''')
        assert output[-1] == "true"
