"""
Tests for number .abundance() method - aliquotSum - n.
"""

from silk.interpreter import Interpreter


class TestNumberAbundance:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_abundance_12(self):
        output = self._run('print(12.abundance())')
        assert output[-1] == "4"

    def test_abundance_10(self):
        output = self._run('print(10.abundance())')
        assert output[-1] == "-2"
