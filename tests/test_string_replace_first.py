"""
Tests for string .replaceFirst() method.
"""

from silk.interpreter import Interpreter


class TestStringReplaceFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_replaceFirst_basic(self):
        output = self._run('''
print("aaa bbb aaa".replaceFirst("aaa", "ccc"))
''')
        assert output[-1] == "ccc bbb aaa"

    def test_replaceFirst_no_match(self):
        output = self._run('''
print("hello".replaceFirst("xyz", "abc"))
''')
        assert output[-1] == "hello"

    def test_replaceFirst_empty(self):
        output = self._run('''
print("hello".replaceFirst("l", ""))
''')
        assert output[-1] == "helo"
