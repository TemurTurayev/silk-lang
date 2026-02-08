"""
Tests for number .isRough(k) method - k-rough number check.
Smallest prime factor is >= k.
"""

from silk.interpreter import Interpreter


class TestNumberIsRough:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isRough_7_5(self):
        output = self._run('print(7.isRough(5))')
        assert output[-1] == "true"

    def test_isRough_25_5(self):
        output = self._run('print(25.isRough(5))')
        assert output[-1] == "true"

    def test_isRough_15_5(self):
        output = self._run('print(15.isRough(5))')
        assert output[-1] == "false"
