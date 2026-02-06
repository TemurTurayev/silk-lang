"""
Tests for string .lastIndexOf() method.
"""

from silk.interpreter import Interpreter


class TestStringLastIndex:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lastIndexOf_found(self):
        output = self._run('''
print("hello world hello".lastIndexOf("hello"))
''')
        assert output[-1] == "12"

    def test_lastIndexOf_single(self):
        output = self._run('''
print("abcdef".lastIndexOf("cd"))
''')
        assert output[-1] == "2"

    def test_lastIndexOf_not_found(self):
        output = self._run('''
print("hello".lastIndexOf("xyz"))
''')
        assert output[-1] == "-1"
