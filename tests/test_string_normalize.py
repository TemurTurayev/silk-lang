"""
Tests for string .normalize() method.
"""

from silk.interpreter import Interpreter


class TestStringNormalize:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_normalize_spaces(self):
        output = self._run('print("  hello   world  ".normalize())')
        assert output[-1] == "hello world"

    def test_normalize_tabs(self):
        output = self._run(r'print("hello\tworld".normalize())')
        assert output[-1] == "hello world"

    def test_normalize_already_clean(self):
        output = self._run('print("hello world".normalize())')
        assert output[-1] == "hello world"
