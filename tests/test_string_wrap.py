"""
Tests for string .wrap() method.
"""

from silk.interpreter import Interpreter


class TestStringWrap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_wrap_basic(self):
        output = self._run('''
print("hello".wrap("(", ")"))
''')
        assert output[-1] == "(hello)"

    def test_wrap_html(self):
        output = self._run('''
print("text".wrap("<b>", "</b>"))
''')
        assert output[-1] == "<b>text</b>"

    def test_wrap_same(self):
        output = self._run('''
print("hello".wrap("*", "*"))
''')
        assert output[-1] == "*hello*"
