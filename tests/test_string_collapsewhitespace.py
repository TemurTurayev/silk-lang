"""
Tests for string .collapseWhitespace() method.
"""

from silk.interpreter import Interpreter


class TestStringCollapseWhitespace:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_collapseWhitespace_spaces(self):
        output = self._run('print("hello    world".collapseWhitespace())')
        assert output[-1] == "hello world"

    def test_collapseWhitespace_mixed(self):
        output = self._run(r'print("hello\t\n  world".collapseWhitespace())')
        assert output[-1] == "hello world"

    def test_collapseWhitespace_already_clean(self):
        output = self._run('print("hello world".collapseWhitespace())')
        assert output[-1] == "hello world"
