"""
Tests for number .isAmicable() method - check if number is part of an amicable pair.
Amicable pairs: (220, 284), (1184, 1210), etc.
"""

from silk.interpreter import Interpreter


class TestNumberIsAmicable:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAmicable_220(self):
        output = self._run('print(220.isAmicable())')
        assert output[-1] == "true"

    def test_isAmicable_10(self):
        output = self._run('print(10.isAmicable())')
        assert output[-1] == "false"
