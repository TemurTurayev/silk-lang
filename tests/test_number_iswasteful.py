"""
Tests for number .isWasteful() method - prime factorization uses more digits than n.
"""

from silk.interpreter import Interpreter


class TestNumberIsWasteful:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isWasteful_4(self):
        output = self._run('print(4.isWasteful())')
        assert output[-1] == "true"

    def test_isWasteful_2(self):
        output = self._run('print(2.isWasteful())')
        assert output[-1] == "false"
