"""
Tests for string .toScreamingKebab() method - SCREAMING-KEBAB-CASE.
"""

from silk.interpreter import Interpreter


class TestStringToScreamingKebab:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toScreamingKebab_basic(self):
        output = self._run('print("hello world".toScreamingKebab())')
        assert output[-1] == "HELLO-WORLD"

    def test_toScreamingKebab_single(self):
        output = self._run('print("foo".toScreamingKebab())')
        assert output[-1] == "FOO"
