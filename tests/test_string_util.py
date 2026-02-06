"""
Tests for string .replaceAll() and .includes() methods.
"""

from silk.interpreter import Interpreter


class TestStringReplaceAll:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_replaceAll_basic(self):
        output = self._run('print("a-b-c".replaceAll("-", " "))')
        assert output[-1] == "a b c"

    def test_replaceAll_multiple(self):
        output = self._run('print("hello world hello".replaceAll("hello", "hi"))')
        assert output[-1] == "hi world hi"

    def test_replaceAll_no_match(self):
        output = self._run('print("abc".replaceAll("x", "y"))')
        assert output[-1] == "abc"

    def test_replaceAll_empty(self):
        output = self._run('print("aaa".replaceAll("a", ""))')
        assert output[-1] == ""


class TestStringIncludes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_includes_true(self):
        output = self._run('print("hello world".includes("world"))')
        assert output[-1] == "true"

    def test_includes_false(self):
        output = self._run('print("hello".includes("xyz"))')
        assert output[-1] == "false"

    def test_includes_empty(self):
        output = self._run('print("hello".includes(""))')
        assert output[-1] == "true"

    def test_includes_self(self):
        output = self._run('print("abc".includes("abc"))')
        assert output[-1] == "true"
