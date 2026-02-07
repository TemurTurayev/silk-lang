"""
Tests for dict .toSQLDelete(table) method.
"""

from silk.interpreter import Interpreter


class TestDictToSQLDelete:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQLDelete_basic(self):
        output = self._run('''
let d = {"id": 5}
let sql = d.toSQLDelete("users")
print(sql)
''')
        assert output[-1] == "DELETE FROM users WHERE id = 5"

    def test_toSQLDelete_multi(self):
        output = self._run('''
let d = {"name": "Bob", "age": 30}
let sql = d.toSQLDelete("users")
print(sql.starts_with("DELETE FROM users WHERE"))
''')
        assert output[-1] == "true"
