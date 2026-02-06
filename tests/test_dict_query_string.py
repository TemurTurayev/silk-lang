"""
Tests for dict .toQueryString() method.
"""

from silk.interpreter import Interpreter


class TestDictToQueryString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toQueryString_basic(self):
        output = self._run('''
let d = {"name": "alice", "age": 30}
let qs = d.toQueryString()
print(qs.contains("name=alice"))
print(qs.contains("age=30"))
''')
        assert output[0] == "true"
        assert output[1] == "true"

    def test_toQueryString_single(self):
        output = self._run('''
print({"key": "value"}.toQueryString())
''')
        assert output[-1] == "key=value"
