"""
Tests for min, max, abs builtins.
"""

from silk.interpreter import Interpreter


class TestMinMaxAbs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_abs_positive(self):
        output = self._run('print(abs(5))')
        assert output[-1] == "5"

    def test_abs_negative(self):
        output = self._run('print(abs(-7))')
        assert output[-1] == "7"

    def test_abs_zero(self):
        output = self._run('print(abs(0))')
        assert output[-1] == "0"

    def test_abs_float(self):
        output = self._run('print(abs(-3.14))')
        assert output[-1] == "3.14"

    def test_min_two(self):
        output = self._run('print(min(3, 7))')
        assert output[-1] == "3"

    def test_min_multiple(self):
        output = self._run('print(min(5, 2, 8, 1, 9))')
        assert output[-1] == "1"

    def test_min_array(self):
        output = self._run('print(min([10, 3, 7]))')
        assert output[-1] == "3"

    def test_max_two(self):
        output = self._run('print(max(3, 7))')
        assert output[-1] == "7"

    def test_max_multiple(self):
        output = self._run('print(max(5, 2, 8, 1, 9))')
        assert output[-1] == "9"

    def test_max_array(self):
        output = self._run('print(max([10, 3, 7]))')
        assert output[-1] == "10"

    def test_min_strings(self):
        output = self._run('print(min("banana", "apple"))')
        assert output[-1] == "apple"

    def test_max_negative(self):
        output = self._run('print(max(-5, -2, -8))')
        assert output[-1] == "-2"
