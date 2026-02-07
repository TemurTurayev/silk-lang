"""
Tests for number .bell() method - Bell number.
"""

from silk.interpreter import Interpreter


class TestNumberBell:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_bell_0(self):
        output = self._run('print(0.bell())')
        assert output[-1] == "1"

    def test_bell_3(self):
        output = self._run('print(3.bell())')
        assert output[-1] == "5"

    def test_bell_5(self):
        output = self._run('print(5.bell())')
        assert output[-1] == "52"
