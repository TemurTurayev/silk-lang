"""
Tests for string .slice() method.
"""

from silk.interpreter import Interpreter


class TestStringSlice:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_slice_basic(self):
        output = self._run('''
print("hello world".slice(0, 5))
''')
        assert output[-1] == "hello"

    def test_slice_middle(self):
        output = self._run('''
print("hello world".slice(6, 11))
''')
        assert output[-1] == "world"

    def test_slice_from_start(self):
        output = self._run('''
print("abcdef".slice(0, 3))
''')
        assert output[-1] == "abc"

    def test_slice_to_end(self):
        output = self._run('''
print("abcdef".slice(3, 6))
''')
        assert output[-1] == "def"
