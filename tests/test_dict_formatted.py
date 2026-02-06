"""
Tests for dict .toFormattedString() method.
"""

from silk.interpreter import Interpreter


class TestDictToFormattedString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFormattedString_basic(self):
        output = self._run('''
let d = {"name": "alice"}
print(d.toFormattedString())
''')
        assert "name: alice" in output[-1]

    def test_toFormattedString_multi(self):
        output = self._run('''
let d = {"a": 1, "b": 2}
let s = d.toFormattedString()
print(s.contains("a: 1"))
print(s.contains("b: 2"))
''')
        assert output[0] == "true"
        assert output[1] == "true"
