"""
Tests for dict .get(key, default) method.
"""

from silk.interpreter import Interpreter


class TestDictGet:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_get_existing(self):
        output = self._run('''
let m = {"name": "Alice"}
print(m.get("name", "unknown"))
''')
        assert output[-1] == "Alice"

    def test_get_missing(self):
        output = self._run('''
let m = {"name": "Alice"}
print(m.get("age", 0))
''')
        assert output[-1] == "0"

    def test_get_missing_string_default(self):
        output = self._run('''
let m = {:}
print(m.get("host", "localhost"))
''')
        assert output[-1] == "localhost"

    def test_get_null_value(self):
        output = self._run('''
let m = {"x": null}
print(m.get("x", 42))
''')
        assert output[-1] == "null"
