"""
Tests for dict .toSQLWhere(table) method.
"""

from silk.interpreter import Interpreter


class TestDictToSQLWhere:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQLWhere_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let sql = d.toSQLWhere("users")
print(sql)
''')
        assert output[-1] == "SELECT * FROM users WHERE name = Bob"

    def test_toSQLWhere_multi(self):
        output = self._run('''
let d = {"id": 1, "active": true}
let sql = d.toSQLWhere("users")
print(sql.starts_with("SELECT * FROM users WHERE"))
''')
        assert output[-1] == "true"
