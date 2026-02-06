"""
Tests for multi-line string support (triple quotes).

Syntax: \"\"\"multi
line
string\"\"\"
"""

from silk.interpreter import Interpreter


class TestMultiLineString:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_multiline(self):
        output = self._run('''
let s = """hello
world"""
print(s.length)
''')
        assert output[-1] == "11"

    def test_multiline_contains_newline(self):
        output = self._run('''
let s = """line1
line2"""
print(s.includes("\\n"))
''')
        assert output[-1] == "true"

    def test_multiline_split_lines(self):
        output = self._run('''
let s = """a
b
c"""
let lines = s.split("\\n")
print(lines.length)
''')
        assert output[-1] == "3"

    def test_multiline_in_variable(self):
        output = self._run('''
let msg = """Dear user,
Thank you."""
print(msg.starts_with("Dear"))
''')
        assert output[-1] == "true"

    def test_multiline_empty(self):
        output = self._run('''
let s = """"""
print(s.isEmpty())
''')
        assert output[-1] == "true"

    def test_multiline_single_line(self):
        output = self._run('''
let s = """just one line"""
print(s)
''')
        assert output[-1] == "just one line"
