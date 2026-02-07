"""
Tests for dict .toJSONPretty() method.
"""

from silk.interpreter import Interpreter


class TestDictToJSONPretty:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toJSONPretty_has_indent(self):
        output = self._run('''
let d = {"name": "Bob"}
let j = d.toJSONPretty()
print(j.contains("  "))
''')
        assert output[-1] == "true"

    def test_toJSONPretty_has_braces(self):
        output = self._run('''
let d = {"x": 1}
let j = d.toJSONPretty()
print(j.starts_with("{"))
''')
        assert output[-1] == "true"
