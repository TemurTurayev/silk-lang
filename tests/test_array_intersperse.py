"""
Tests for array .intersperse(val) method.
"""

from silk.interpreter import Interpreter


class TestArrayIntersperse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_intersperse_basic(self):
        output = self._run('print([1, 2, 3].intersperse(0))')
        assert output[-1] == "[1, 0, 2, 0, 3]"

    def test_intersperse_strings(self):
        output = self._run('print(["a", "b", "c"].intersperse("-"))')
        assert output[-1] == '[a, -, b, -, c]'

    def test_intersperse_single(self):
        output = self._run('print([1].intersperse(0))')
        assert output[-1] == "[1]"
