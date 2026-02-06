"""
Tests for string .toUpper() and .toLower() aliases.
"""

from silk.interpreter import Interpreter


class TestStringToUpper:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toUpper(self):
        output = self._run('''
print("hello".toUpper())
''')
        assert output[-1] == "HELLO"

    def test_toUpper_mixed(self):
        output = self._run('''
print("Hello World".toUpper())
''')
        assert output[-1] == "HELLO WORLD"


class TestStringToLower:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toLower(self):
        output = self._run('''
print("HELLO".toLower())
''')
        assert output[-1] == "hello"

    def test_toLower_mixed(self):
        output = self._run('''
print("Hello World".toLower())
''')
        assert output[-1] == "hello world"
