"""
Tests for dict .toJson() method.
"""

from silk.interpreter import Interpreter


class TestDictJson:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toJson_basic(self):
        output = self._run('''
let m = {"name": "silk"}
let j = m.toJson()
print(typeof j)
''')
        assert output[-1] == "string"

    def test_toJson_contains_key(self):
        output = self._run('''
let m = {"key": "value"}
let j = m.toJson()
print(j.contains("key"))
print(j.contains("value"))
''')
        assert output[-2] == "true"
        assert output[-1] == "true"

    def test_toJson_empty(self):
        output = self._run('''
let m = {:}
print(m.toJson())
''')
        assert output[-1] == "{}"
