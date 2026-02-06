"""
Tests for string .squeeze() method.
"""

from silk.interpreter import Interpreter


class TestStringSqueeze:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_squeeze_spaces(self):
        output = self._run('''
print("hello   world   foo".squeeze())
''')
        assert output[-1] == "hello world foo"

    def test_squeeze_no_change(self):
        output = self._run('''
print("hello world".squeeze())
''')
        assert output[-1] == "hello world"

    def test_squeeze_leading_trailing(self):
        output = self._run('''
print("  hello  ".squeeze())
''')
        assert output[-1] == " hello "
