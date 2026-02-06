"""
Tests for string .format() template method.
"""

from silk.interpreter import Interpreter


class TestStringFormat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_format_basic(self):
        output = self._run('''
let template = "Hello, {}!"
print(template.format("world"))
''')
        assert output[-1] == "Hello, world!"

    def test_format_multiple(self):
        output = self._run('''
let template = "{} + {} = {}"
print(template.format("1", "2", "3"))
''')
        assert output[-1] == "1 + 2 = 3"

    def test_format_numbers(self):
        output = self._run('''
print("Value: {}".format(42))
''')
        assert output[-1] == "Value: 42"

    def test_format_no_placeholders(self):
        output = self._run('''
print("no placeholders".format("ignored"))
''')
        assert output[-1] == "no placeholders"
