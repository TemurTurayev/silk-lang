"""
Tests for string .mirror() method.
"""

from silk.interpreter import Interpreter


class TestStringMirror:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mirror_basic(self):
        output = self._run('print("abc".mirror())')
        assert output[-1] == "abccba"

    def test_mirror_single(self):
        output = self._run('print("x".mirror())')
        assert output[-1] == "xx"
