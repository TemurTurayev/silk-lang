"""
Tests for number .isAmicable(other) method.
"""

from silk.interpreter import Interpreter


class TestNumberIsAmicable:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAmicable_220_284(self):
        output = self._run('print(220.isAmicable(284))')
        assert output[-1] == "true"

    def test_isAmicable_not(self):
        output = self._run('print(10.isAmicable(20))')
        assert output[-1] == "false"

    def test_isAmicable_reverse(self):
        output = self._run('print(284.isAmicable(220))')
        assert output[-1] == "true"
