"""
Tests for dict .toHeaderString() method - HTTP-style header format.
"""

from silk.interpreter import Interpreter


class TestDictToHeaderString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHeaderString_basic(self):
        output = self._run('''
let h = {"Content-Type": "application/json"}
print(h.toHeaderString())
''')
        assert output[-1] == "Content-Type: application/json"

    def test_toHeaderString_multiple(self):
        output = self._run('''
let h = {"Host": "example.com", "Accept": "text/html"}
let s = h.toHeaderString()
print(s.contains("Host: example.com"))
''')
        assert output[-1] == "true"
