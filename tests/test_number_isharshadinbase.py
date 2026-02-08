"""
Tests for number .isHarshadInBase(base) method - Harshad number in given base.
"""

from silk.interpreter import Interpreter


class TestNumberIsHarshadInBase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isHarshadInBase_10(self):
        output = self._run('print(18.isHarshadInBase(10))')
        assert output[-1] == "true"

    def test_isHarshadInBase_16(self):
        output = self._run('print(18.isHarshadInBase(16))')
        assert output[-1] == "true"

    def test_isHarshadInBase_false(self):
        output = self._run('print(13.isHarshadInBase(10))')
        assert output[-1] == "false"
