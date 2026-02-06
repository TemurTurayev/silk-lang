"""
Tests for string .isUpper() and .isLower() methods.
"""

from silk.interpreter import Interpreter


class TestStringCaseCheck:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isUpper_true(self):
        output = self._run('''
print("HELLO".isUpper())
''')
        assert output[-1] == "true"

    def test_isUpper_false(self):
        output = self._run('''
print("Hello".isUpper())
''')
        assert output[-1] == "false"

    def test_isLower_true(self):
        output = self._run('''
print("hello".isLower())
''')
        assert output[-1] == "true"

    def test_isLower_false(self):
        output = self._run('''
print("Hello".isLower())
''')
        assert output[-1] == "false"

    def test_isUpper_empty(self):
        output = self._run('''
print("".isUpper())
''')
        assert output[-1] == "false"

    def test_isLower_empty(self):
        output = self._run('''
print("".isLower())
''')
        assert output[-1] == "false"
