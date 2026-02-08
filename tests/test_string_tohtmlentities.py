"""
Tests for string .toHTMLEntities() method - convert special chars to HTML entities.
"""

from silk.interpreter import Interpreter


class TestStringToHTMLEntities:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toHTMLEntities_amp(self):
        output = self._run('print("a&b".toHTMLEntities())')
        assert output[-1] == "a&amp;b"

    def test_toHTMLEntities_lt(self):
        output = self._run('print("<div>".toHTMLEntities())')
        assert output[-1] == "&lt;div&gt;"
