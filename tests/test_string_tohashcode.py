"""
Tests for string .toHashCode() method.
"""

from silk.interpreter import Interpreter


class TestStringToHashCode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHashCode_basic(self):
        output = self._run('print("hello".toHashCode())')
        assert output[-1] == str(hash("hello"))

    def test_toHashCode_empty(self):
        output = self._run('print("".toHashCode())')
        assert output[-1] == str(hash(""))

    def test_toHashCode_same_string(self):
        output = self._run('''
let a = "test".toHashCode()
let b = "test".toHashCode()
print(a == b)
''')
        assert output[-1] == "true"
