"""
Tests for number .lcm() method.
"""

from silk.interpreter import Interpreter


class TestNumberLcm:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lcm_basic(self):
        output = self._run('print(4.lcm(6))')
        assert output[-1] == "12"

    def test_lcm_coprime(self):
        output = self._run('print(3.lcm(7))')
        assert output[-1] == "21"

    def test_lcm_same(self):
        output = self._run('print(5.lcm(5))')
        assert output[-1] == "5"
