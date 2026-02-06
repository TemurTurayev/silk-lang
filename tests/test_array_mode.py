"""
Tests for array .mode() method.
"""

from silk.interpreter import Interpreter


class TestArrayMode:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mode_single(self):
        output = self._run('print([1, 2, 2, 3].mode())')
        assert output[-1] == "[2]"

    def test_mode_multiple(self):
        output = self._run('print([1, 1, 2, 2, 3].mode())')
        assert output[-1] == "[1, 2]"

    def test_mode_all_same(self):
        output = self._run('print([5, 5, 5].mode())')
        assert output[-1] == "[5]"
