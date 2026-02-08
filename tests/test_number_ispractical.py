"""
Tests for number .isPractical() method - check if every number up to n can be represented as sum of distinct divisors.
"""

from silk.interpreter import Interpreter


class TestNumberIsPractical:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPractical_6(self):
        output = self._run('print(6.isPractical())')
        assert output[-1] == "true"

    def test_isPractical_5(self):
        output = self._run('print(5.isPractical())')
        assert output[-1] == "false"
