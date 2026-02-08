"""
Tests for number .isSophieGermain() method - prime where 2p+1 is also prime.
"""

from silk.interpreter import Interpreter


class TestNumberIsSophieGermain:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSophieGermain_5(self):
        output = self._run('print(5.isSophieGermain())')
        assert output[-1] == "true"

    def test_isSophieGermain_7(self):
        output = self._run('print(7.isSophieGermain())')
        assert output[-1] == "false"
