"""
Tests for string .surround(s) method.
"""

from silk.interpreter import Interpreter


class TestStringSurround:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_surround_basic(self):
        output = self._run('print("hello".surround("**"))')
        assert output[-1] == "**hello**"

    def test_surround_quote(self):
        output = self._run("""print("world".surround("'"))""")
        assert output[-1] == "'world'"
