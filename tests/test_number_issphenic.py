"""
Tests for number .isSphenic() method - product of 3 distinct primes.
"""

from silk.interpreter import Interpreter


class TestNumberIsSphenic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSphenic_30(self):
        output = self._run('print(30.isSphenic())')
        assert output[-1] == "true"

    def test_isSphenic_12(self):
        output = self._run('print(12.isSphenic())')
        assert output[-1] == "false"

    def test_isSphenic_66(self):
        output = self._run('print(66.isSphenic())')
        assert output[-1] == "true"
