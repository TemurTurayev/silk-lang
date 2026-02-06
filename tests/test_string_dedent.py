"""
Tests for string .dedent() method.
"""

from silk.interpreter import Interpreter


class TestStringDedent:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dedent_basic(self):
        output = self._run('''
let s = "  hello\\n  world"
print(s.dedent())
''')
        assert output[-1] == "hello\nworld"

    def test_dedent_mixed_indent(self):
        output = self._run('''
let s = "    a\\n  b\\n    c"
print(s.dedent())
''')
        assert output[-1] == "  a\nb\n  c"
