"""
Tests for string .padCenter() method.
"""

from silk.interpreter import Interpreter


class TestStringPadCenter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_padCenter_basic(self):
        output = self._run('''
print("hi".padCenter(6, "*"))
''')
        assert output[-1] == "**hi**"

    def test_padCenter_odd(self):
        output = self._run('''
print("ab".padCenter(5, "-"))
''')
        assert output[-1] == "--ab-"

    def test_padCenter_no_pad_needed(self):
        output = self._run('''
print("hello".padCenter(3, "*"))
''')
        assert output[-1] == "hello"
