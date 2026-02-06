"""
Tests for string .removePrefix(), .removeSuffix(), .truncate() methods.
"""

from silk.interpreter import Interpreter


class TestStringRemove:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removePrefix(self):
        output = self._run('''
print("hello world".removePrefix("hello "))
''')
        assert output[-1] == "world"

    def test_removePrefix_no_match(self):
        output = self._run('''
print("hello".removePrefix("xyz"))
''')
        assert output[-1] == "hello"

    def test_removeSuffix(self):
        output = self._run('''
print("hello.silk".removeSuffix(".silk"))
''')
        assert output[-1] == "hello"

    def test_removeSuffix_no_match(self):
        output = self._run('''
print("hello".removeSuffix(".silk"))
''')
        assert output[-1] == "hello"

    def test_truncate_basic(self):
        output = self._run('''
print("hello world foo bar".truncate(10, "..."))
''')
        assert output[-1] == "hello w..."

    def test_truncate_short_string(self):
        output = self._run('''
print("hi".truncate(10, "..."))
''')
        assert output[-1] == "hi"

    def test_truncate_exact(self):
        output = self._run('''
print("hello".truncate(5, "..."))
''')
        assert output[-1] == "hello"
