"""
Tests for string .squeezeBlanks() method - collapse blank lines.
"""

from silk.interpreter import Interpreter


class TestStringSqueezeBlanks:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_squeezeBlanks_basic(self):
        output = self._run('print("a\\n\\n\\nb".squeezeBlanks().contains("\\n\\n\\n"))')
        assert output[-1] == "false"

    def test_squeezeBlanks_keeps_single(self):
        output = self._run('print("a\\nb".squeezeBlanks())')
        assert output[-1] == "a\nb"
