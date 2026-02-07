"""
Tests for number .lucas() method - Lucas number at index n.
"""

from silk.interpreter import Interpreter


class TestNumberLucas:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lucas_5(self):
        output = self._run('print(5.lucas())')
        assert output[-1] == "11"

    def test_lucas_0(self):
        output = self._run('print(0.lucas())')
        assert output[-1] == "2"
