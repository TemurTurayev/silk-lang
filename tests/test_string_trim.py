"""
Tests for string .trim_start() and .trim_end() methods.
"""

from silk.interpreter import Interpreter


class TestStringTrimStart:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_trim_start(self):
        output = self._run('''
print("  hello".trim_start())
''')
        assert output[-1] == "hello"

    def test_trim_start_tabs(self):
        output = self._run('''
let s = "	hello"
print(s.trim_start())
''')
        assert output[-1] == "hello"

    def test_trim_start_no_space(self):
        output = self._run('''
print("hello".trim_start())
''')
        assert output[-1] == "hello"


class TestStringTrimEnd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_trim_end(self):
        output = self._run('''
print("hello  ".trim_end())
''')
        assert output[-1] == "hello"

    def test_trim_end_no_space(self):
        output = self._run('''
print("hello".trim_end())
''')
        assert output[-1] == "hello"

    def test_trim_both(self):
        output = self._run('''
let s = "  hello  "
print(s.trim_start().trim_end())
''')
        assert output[-1] == "hello"
