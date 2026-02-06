"""
Tests for string .commonPrefix() and .commonSuffix() methods.
"""

from silk.interpreter import Interpreter


class TestStringCommon:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_commonPrefix_basic(self):
        output = self._run('''
print("hello".commonPrefix("help"))
''')
        assert output[-1] == "hel"

    def test_commonPrefix_none(self):
        output = self._run('''
print("abc".commonPrefix("xyz"))
''')
        assert output[-1] == ""

    def test_commonPrefix_full(self):
        output = self._run('''
print("test".commonPrefix("test"))
''')
        assert output[-1] == "test"

    def test_commonSuffix_basic(self):
        output = self._run('''
print("testing".commonSuffix("running"))
''')
        assert output[-1] == "ing"

    def test_commonSuffix_none(self):
        output = self._run('''
print("abc".commonSuffix("xyz"))
''')
        assert output[-1] == ""
