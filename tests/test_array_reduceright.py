"""
Tests for array .reduceRight(fn, init) method.
"""

from silk.interpreter import Interpreter


class TestArrayReduceRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reduceRight_concat(self):
        output = self._run('print(["a", "b", "c"].reduceRight(|acc, x| acc + x, ""))')
        assert output[-1] == "cba"

    def test_reduceRight_subtract(self):
        output = self._run('print([1, 2, 3].reduceRight(|acc, x| acc - x, 10))')
        assert output[-1] == "4"
