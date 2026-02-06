"""
Tests for string .center() and .lines() methods.
"""

from silk.interpreter import Interpreter


class TestStringPad:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_center_basic(self):
        output = self._run('''
print("hi".center(10, "*"))
''')
        assert output[-1] == "****hi****"

    def test_center_odd(self):
        output = self._run('''
print("abc".center(7, "-"))
''')
        assert output[-1] == "--abc--"

    def test_center_no_padding_needed(self):
        output = self._run('''
print("hello".center(3, " "))
''')
        assert output[-1] == "hello"


class TestStringLines:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lines_basic(self):
        output = self._run('''
let text = """line1
line2
line3"""
let parts = text.lines()
print(parts.length)
''')
        assert output[-1] == "3"

    def test_lines_content(self):
        output = self._run('''
let text = """hello
world"""
let parts = text.lines()
print(parts[0])
print(parts[1])
''')
        assert output[-2] == "hello"
        assert output[-1] == "world"
