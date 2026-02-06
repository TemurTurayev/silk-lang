"""
Tests for string .charAt() and .charCodeAt() methods.
"""

from silk.interpreter import Interpreter


class TestStringCharAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_charAt_basic(self):
        output = self._run('''
print("hello".charAt(0))
''')
        assert output[-1] == "h"

    def test_charAt_middle(self):
        output = self._run('''
print("hello".charAt(2))
''')
        assert output[-1] == "l"

    def test_charAt_last(self):
        output = self._run('''
print("abc".charAt(2))
''')
        assert output[-1] == "c"


class TestStringCharCodeAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_charCodeAt_a(self):
        output = self._run('''
print("a".charCodeAt(0))
''')
        assert output[-1] == "97"

    def test_charCodeAt_A(self):
        output = self._run('''
print("A".charCodeAt(0))
''')
        assert output[-1] == "65"

    def test_charCodeAt_digit(self):
        output = self._run('''
print("0".charCodeAt(0))
''')
        assert output[-1] == "48"

    def test_charCodeAt_middle(self):
        output = self._run('''
print("hello".charCodeAt(1))
''')
        assert output[-1] == "101"
