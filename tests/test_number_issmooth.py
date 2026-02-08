"""
Tests for number .isSmooth(k) method - k-smooth number check.
All prime factors are <= k.
"""

from silk.interpreter import Interpreter


class TestNumberIsSmooth:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSmooth_8_3(self):
        output = self._run('print(8.isSmooth(3))')
        assert output[-1] == "true"

    def test_isSmooth_15_5(self):
        output = self._run('print(15.isSmooth(5))')
        assert output[-1] == "true"

    def test_isSmooth_15_3(self):
        output = self._run('print(15.isSmooth(3))')
        assert output[-1] == "false"
