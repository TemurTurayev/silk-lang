"""
Tests for string .zfill(width) method.
"""

from silk.interpreter import Interpreter


class TestStringZfill:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zfill_basic(self):
        output = self._run('''
print("42".zfill(5))
''')
        assert output[-1] == "00042"

    def test_zfill_already_wide(self):
        output = self._run('''
print("hello".zfill(3))
''')
        assert output[-1] == "hello"

    def test_zfill_exact(self):
        output = self._run('''
print("abc".zfill(3))
''')
        assert output[-1] == "abc"

    def test_zfill_single_char(self):
        output = self._run('''
print("7".zfill(4))
''')
        assert output[-1] == "0007"
