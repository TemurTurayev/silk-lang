"""
Tests for dict .toSQLUpdate(table) method.
"""

from silk.interpreter import Interpreter


class TestDictToSQLUpdate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQLUpdate_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let sql = d.toSQLUpdate("users")
print(sql)
''')
        assert output[-1] == "UPDATE users SET name = Bob"

    def test_toSQLUpdate_multi(self):
        output = self._run('''
let d = {"x": 1, "y": 2}
let sql = d.toSQLUpdate("t")
print(sql.starts_with("UPDATE t SET"))
''')
        assert output[-1] == "true"
