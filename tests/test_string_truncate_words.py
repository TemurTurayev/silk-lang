"""
Tests for string .truncateWords(n) method.
"""

from silk.interpreter import Interpreter


class TestStringTruncateWords:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_truncateWords_basic(self):
        output = self._run('''
print("the quick brown fox jumps".truncateWords(3))
''')
        assert output[-1] == "the quick brown..."

    def test_truncateWords_all(self):
        output = self._run('''
print("hello world".truncateWords(5))
''')
        assert output[-1] == "hello world"

    def test_truncateWords_one(self):
        output = self._run('''
print("alpha beta gamma".truncateWords(1))
''')
        assert output[-1] == "alpha..."
