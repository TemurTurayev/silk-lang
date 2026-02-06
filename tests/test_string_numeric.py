"""
Tests for string .isNumeric() method.
"""

from silk.interpreter import Interpreter


class TestStringNumeric:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isNumeric_integer(self):
        output = self._run('''
print("123".isNumeric())
''')
        assert output[-1] == "true"

    def test_isNumeric_float(self):
        output = self._run('''
print("3.14".isNumeric())
''')
        assert output[-1] == "true"

    def test_isNumeric_negative(self):
        output = self._run('''
print("-42".isNumeric())
''')
        assert output[-1] == "true"

    def test_isNumeric_false(self):
        output = self._run('''
print("abc".isNumeric())
''')
        assert output[-1] == "false"

    def test_isNumeric_empty(self):
        output = self._run('''
print("".isNumeric())
''')
        assert output[-1] == "false"

    def test_isNumeric_mixed(self):
        output = self._run('''
print("12ab".isNumeric())
''')
        assert output[-1] == "false"
