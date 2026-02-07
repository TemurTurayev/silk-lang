"""
Tests for dict .toSQLInsert(table) method.
"""

from silk.interpreter import Interpreter


class TestDictToSQLInsert:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQLInsert_basic(self):
        output = self._run('''
let d = {"name": "Alice", "age": 30}
let sql = d.toSQLInsert("users")
print(sql.starts_with("INSERT INTO users"))
''')
        assert output[-1] == "true"

    def test_toSQLInsert_values(self):
        output = self._run('''
let d = {"x": 1}
let sql = d.toSQLInsert("t")
print(sql)
''')
        assert output[-1] == "INSERT INTO t (x) VALUES (1)"
