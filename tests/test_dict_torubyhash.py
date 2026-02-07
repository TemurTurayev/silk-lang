"""
Tests for dict .toRubyHash() method.
"""

from silk.interpreter import Interpreter


class TestDictToRubyHash:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRubyHash_basic(self):
        output = self._run('''
let d = {"name": "Bob"}
let rb = d.toRubyHash()
print(rb.contains("=>"))
''')
        assert output[-1] == "true"

    def test_toRubyHash_braces(self):
        output = self._run('''
let d = {"x": 1}
let rb = d.toRubyHash()
print(rb.starts_with("{"))
''')
        assert output[-1] == "true"
