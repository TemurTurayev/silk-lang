"""
Tests for string .count() and .isDigit() methods.
"""

from silk.interpreter import Interpreter


class TestStringCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_count_char(self):
        output = self._run('''
print("hello".count("l"))
''')
        assert output[-1] == "2"

    def test_count_substring(self):
        output = self._run('''
print("banana".count("an"))
''')
        assert output[-1] == "2"

    def test_count_none(self):
        output = self._run('''
print("hello".count("z"))
''')
        assert output[-1] == "0"

    def test_count_empty(self):
        output = self._run('''
print("".count("a"))
''')
        assert output[-1] == "0"


class TestStringIsDigit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isDigit_true(self):
        output = self._run('''
print("123".isDigit())
''')
        assert output[-1] == "true"

    def test_isDigit_false(self):
        output = self._run('''
print("12a".isDigit())
''')
        assert output[-1] == "false"

    def test_isDigit_empty(self):
        output = self._run('''
print("".isDigit())
''')
        assert output[-1] == "false"

    def test_isDigit_single(self):
        output = self._run('''
print("7".isDigit())
''')
        assert output[-1] == "true"

    def test_isAlpha(self):
        output = self._run('''
print("hello".isAlpha())
''')
        assert output[-1] == "true"

    def test_isAlpha_false(self):
        output = self._run('''
print("hello123".isAlpha())
''')
        assert output[-1] == "false"
