"""
Tests for number .gcd() method.
"""

from silk.interpreter import Interpreter


class TestNumberGcd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_gcd_basic(self):
        output = self._run('print(12.gcd(8))')
        assert output[-1] == "4"

    def test_gcd_coprime(self):
        output = self._run('print(7.gcd(13))')
        assert output[-1] == "1"

    def test_gcd_same(self):
        output = self._run('print(10.gcd(10))')
        assert output[-1] == "10"

    def test_gcd_one(self):
        output = self._run('print(1.gcd(100))')
        assert output[-1] == "1"
